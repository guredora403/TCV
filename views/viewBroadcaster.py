﻿# -*- coding: utf-8 -*-
# 配信者情報

import wx
import globalVars
import views.ViewCreator
from logging import getLogger
from views.baseDialog import *

class Dialog(BaseDialog):
	def __init__(self, broadcaster):
		super().__init__()
		self.broadcaster = {
			_("名前"): broadcaster["name"],
			_("ユーザ名"): broadcaster["screen_id"],
			_("レベル"): str(broadcaster["level"]),
			_("自己紹介"): broadcaster["profile"]
		}

	def Initialize(self):
		self.identifier="viewBroadcasterDialog"#このビューを表す文字列
		self.log=getLogger(self.identifier)
		self.log.debug("created")
		super().Initialize(self.app.hMainView.hFrame,_("配信者の情報"))
		self.InstallControls()
		return True


	def InstallControls(self):
		"""いろんなwidgetを設置する。"""
		self.creator=views.ViewCreator.ViewCreator(0,self.panel,self.sizer,wx.VERTICAL,20)
		for key, value in self.broadcaster.items():
			self.creator.inputbox(key, 500, value, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP)
		self.closeButton=self.creator.cancelbutton(_("閉じる(&C)"), None)

	def GetData(self):
		return self.iText.GetLineText(0)
