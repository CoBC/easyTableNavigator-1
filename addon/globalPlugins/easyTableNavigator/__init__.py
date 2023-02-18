# Easy Table Navigator
# A global plugin for NvDA
# Copyright 2015-2022 Joseph Lee, Cyrille Bougot, released under GPL

# Allows NVDA to navigate to next or previous column/row just by using arrow keys.
# The results should be similar to table layer in JAWS.

import globalPluginHandler
import api
import config
import documentBase
from NVDAObjects.window import winword
import textInfos
from . import compa
import controlTypes
import ui
import scriptHandler
import addonHandler
addonHandler.initTranslation()
controlTypes = compa.convertControlTypes(controlTypes)

# Keep a tuple of candidate tree interceptors and object types handy.
TNDocObjs=(
	(winword.WordDocument),
)

# For Microsoft Word: code from MS Word document object, pasted here for convenience.
def _MSWordTableNavAvailable(document):
	if hasattr(document, 'UIAAutomationId'):
		return _MSWordUIATableNavAvailable(document)
	info=document.makeTextInfo(textInfos.POSITION_CARET)
	info.expand(textInfos.UNIT_CHARACTER)
	formatConfig=config.conf['documentFormatting'].copy()
	formatConfig['reportTables']=True
	commandList=info.getTextWithFields(formatConfig)
	if len(commandList)<3 or commandList[1].field.get('role',None)!=controlTypes.Role.TABLE or commandList[2].field.get('role',None)!=controlTypes.Role.TABLECELL:
		return False
	rowCount=commandList[1].field.get('table-rowcount',1)
	columnCount=commandList[1].field.get('table-columncount',1)
	rowNumber=commandList[2].field.get('table-rownumber',1)
	columnNumber=commandList[2].field.get('table-columnnumber',1)
	try:
		table=info._rangeObj.tables[1]
	except COMError:
		return False
	return True

def _MSWordUIATableNavAvailable(document):
	try:
		document._getTableCellCoords(document.selection)
		return True
	except LookupError:
		return False

# For docs, return the needed lookup function based on class name.
# Placed here since Python complains that callable names cannot be found.
TNDocObjTesters={
	"_WwG":_MSWordTableNavAvailable,
}

# Actual table navigator tester (to be called throughout the life of the plugin).
def tableNavAvailable(obj=None):
	# Depending on object type, figure out if we're in a table.
	focus = api.getFocusObject() if obj is None else obj
	if isinstance(focus, TNDocObjs):
		try:
			testFunc = TNDocObjTesters[focus.windowClassName]
		except KeyError:
			return False
		return testFunc(focus)
	elif (
		isinstance(focus.treeInterceptor, documentBase.DocumentWithTableNavigation)
		and not focus.treeInterceptor.passThrough
	):
		try:
			focus.treeInterceptor._getTableCellCoords(focus.treeInterceptor.selection)
			return True
		except (LookupError, WindowsError):
			return False
	return False

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Control table layer entry.
	tableNav = False
	tableNavForFocus = False

	def event_gainFocus(self, obj, nextHandler):
		try:
			if tableNavAvailable(obj) and self.tableNav:
				self.bindTableNavGestures()
			else:
				self.clearGestureBindings()
				self.bindGestures(self.__gestures)
		except WindowsError:
			pass
		nextHandler()

	@scriptHandler.script(
		# Translators: input help mode message for Table Navigator toggle command.
		description=_("Toggles table navigation layer on or off. When active, arrow keys can be used to navigate between cells"),
		# Translators: command category for the add-on.
		category=_("Easy Table Navigator")
	)
	def script_toggleTableNav(self, gesture):
		if not self.tableNav:
			if not tableNavAvailable():
				# Translators: presented when a user is not in a table.
				ui.message(_("Not in a table"))
				return
			self.tableNav = True
			self.bindTableNavGestures()
			# Translators: presented when table navigator layer is on.
			ui.message(_("Table navigator on"))
		else:
			self.tableNav = False
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)
			# Translators: presented when table navigator layer is off.
			ui.message(_("Table navigator off"))

	# Some utility functions.
	def bindTableNavGestures(self):
		self.bindGesture("kb:rightarrow", "nextColumn")
		self.bindGesture("kb:leftarrow", "prevColumn")
		self.bindGesture("kb:downarrow", "nextRow")
		self.bindGesture("kb:uparrow", "prevRow")
		if not hasattr(documentBase.DocumentWithTableNavigation, 'script_firstRow'):
			# In NVDA 2022.2, table navigation commands to jump to first/last row/column have been added.
			# For previous versions of NVDA not supporting them, just return here.
			return
		self.bindGesture("kb:control+rightarrow", "lastColumn")
		self.bindGesture("kb:end", "lastColumn")
		self.bindGesture("kb:control+leftarrow", "firstColumn")
		self.bindGesture("kb:home", "firstColumn")
		self.bindGesture("kb:control+downarrow", "lastRow")
		self.bindGesture("kb:pageDown", "lastRow")
		self.bindGesture("kb:control+uparrow", "firstRow")
		self.bindGesture("kb:pageUp", "firstRow")
		if not hasattr(documentBase.DocumentWithTableNavigation, 'script_speakRow'):
			# In NVDA 2022.4, new table navigation commands have been added:
			# read entire row/column and say all in row/column.
			# For previous versions of NVDA not supporting them, just return here.
			return
		self.bindGesture("kb:windows+rightarrow", "sayAllRow")
		self.bindGesture("kb:windows+downarrow", "sayAllColumn")
		self.bindGesture("kb:windows+leftarrow", "speakRow")
		self.bindGesture("kb:windows+uparrow", "speakColumn")
		
				

	# Table navigation commands.
	
	def tableNavigationHelper(self, gesture, move):
		focus = api.getFocusObject()
		if (
			isinstance(focus.treeInterceptor, documentBase.DocumentWithTableNavigation)
			and not focus.treeInterceptor.passThrough
		):
			getattr(focus.treeInterceptor, f'script_{move}')(gesture)
		else:
			getattr(focus, f'script_{move}')(gesture)

	def script_nextRow(self, gesture):
		self.tableNavigationHelper(gesture, 'nextRow')

	def script_prevRow(self, gesture):
		self.tableNavigationHelper(gesture, 'previousRow')

	def script_nextColumn(self, gesture):
		self.tableNavigationHelper(gesture, 'nextColumn')

	def script_prevColumn(self, gesture):
		self.tableNavigationHelper(gesture, 'previousColumn')
	
	def script_lastRow(self, gesture):
		self.tableNavigationHelper(gesture, 'lastRow')

	def script_firstRow(self, gesture):
		self.tableNavigationHelper(gesture, 'firstRow')

	def script_lastColumn(self, gesture):
		self.tableNavigationHelper(gesture, 'lastColumn')

	def script_firstColumn(self, gesture):
		self.tableNavigationHelper(gesture, 'firstColumn')
	
	def script_sayAllRow(self, gesture):
		self.tableNavigationHelper(gesture, 'sayAllRow')
	
	def script_sayAllColumn(self, gesture):
		self.tableNavigationHelper(gesture, 'sayAllColumn')
	
	def script_speakRow(self, gesture):
		self.tableNavigationHelper(gesture, 'speakRow')
		
	def script_speakColumn(self, gesture):
		self.tableNavigationHelper(gesture, 'speakColumn')
	
	__gestures = {}
