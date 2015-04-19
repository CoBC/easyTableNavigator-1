﻿# Easy Table Navigator
# A global plugin for NvDA
# Copyright 2015 Joseph Lee, released under GPL

# Allows NVDA to navigate to next or previous column/row just by using arrow keys.
# The results should be similar to table layer in JAWS.

import globalPluginHandler
import api
import config
import virtualBuffers # For browse mode.
from NVDAObjects.window import winword # Microsoft Word.
import textInfos
import controlTypes
import addonHandler
import ui
import tones #Debugging

# Keep a tuple of candidate tree interceptors and object types handy.
TNDocObjs=(
	(winword.WordDocument),
)

# For Microsoft Word: code from MS Word document object, pasted here for convenience.
def _MSWordTableNavAvailable(document):
	info=document.makeTextInfo(textInfos.POSITION_CARET)
	info.expand(textInfos.UNIT_CHARACTER)
	formatConfig=config.conf['documentFormatting'].copy()
	formatConfig['reportTables']=True
	commandList=info.getTextWithFields(formatConfig)
	if len(commandList)<3 or commandList[1].field.get('role',None)!=controlTypes.ROLE_TABLE or commandList[2].field.get('role',None)!=controlTypes.ROLE_TABLECELL:
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

# For docs, return the needed lookup function based on class name.
# Placed here since Python complains that callable names cannot be found.
TNDocObjTesters={
	"_WwG":_MSWordTableNavAvailable,
}

# Actual table navigator tester (to be called throughout the life of the plugin).
def tableNavAvailable(obj=None):
	# Depending on object type, figure out if we're in a table.
	focus = api.getFocusObject() if obj is None else obj
	if focus.treeInterceptor and isinstance(focus.treeInterceptor, virtualBuffers.VirtualBuffer):
		try:
			focus.treeInterceptor._getTableCellCoords(focus.treeInterceptor.selection)
			return True
		except LookupError, WindowsError:
			return False
	elif isinstance(focus, TNDocObjs):
		try:
			testFunc = TNDocObjTesters[focus.windowClassName]
		except KeyError:
			return False
		return testFunc(focus)
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

	def script_toggleTableNav(self, gesture):
		if not tableNavAvailable():
			ui.message("Not in a table")
		else:
			if not self.tableNav:
				self.tableNav = True
				self.bindTableNavGestures()
				ui.message("Table navigator on")
			else:
				self.tableNav = False
				self.clearGestureBindings()
				self.bindGestures(self.__gestures)
				ui.message("Table navigator off")
	script_toggleTableNav.__doc__="Toggles table navigation layer on or off. When active, arrow keys can be used to navigate between cells"
	# Since this plugin really has one command, it is fine to define a script category like this.
	script_toggleTableNav.category = "Easy Table Navigator"

	# Some utility functions.
	def bindTableNavGestures(self):
		self.bindGesture("kb:rightarrow", "nextColumn")
		self.bindGesture("kb:leftarrow", "prevColumn")
		self.bindGesture("kb:downarrow", "nextRow")
		self.bindGesture("kb:uparrow", "prevRow")

	def tableNavHelper(self, obj, script, gesture):
		obj.treeInterceptor.script(gesture) if isinstance(obj.treeInterceptor, virtualBuffers.VirtualBuffer) else obj.script(gesture)

	# Table navigation commands.

	def script_nextRow(self, gesture):
		#self.tableNavHelper(api.getFocusObject(), script_nextRow, gesture)
		focus = api.getFocusObject()
		focus.treeInterceptor.script_nextRow(gesture) if isinstance(focus.treeInterceptor, virtualBuffers.VirtualBuffer) else focus.script_nextRow(gesture)

	def script_prevRow(self, gesture):
		#self.tableNavHelper(api.getFocusObject(), script_previousRow, gesture)
		focus = api.getFocusObject()
		focus.treeInterceptor.script_previousRow(gesture) if isinstance(focus.treeInterceptor, virtualBuffers.VirtualBuffer) else focus.script_previousRow(gesture)

	def script_nextColumn(self, gesture):
		#self.tableNavHelper(api.getFocusObject(), script_nextColumn, gesture)
		focus = api.getFocusObject()
		focus.treeInterceptor.script_nextColumn(gesture) if isinstance(focus.treeInterceptor, virtualBuffers.VirtualBuffer) else focus.script_nextColumn(gesture)

	def script_prevColumn(self, gesture):
		#self.tableNavHelper(api.getFocusObject(), script_previousColumn, gesture)
		focus = api.getFocusObject()
		focus.treeInterceptor.script_previousColumn(gesture) if isinstance(focus.treeInterceptor, virtualBuffers.VirtualBuffer) else focus.script_previousColumn(gesture)

	__gestures={
		#"kb:NvDA+Shift+T":"toggleTableNav",
	}
