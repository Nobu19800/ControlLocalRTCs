#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ControlEdison.py
 @brief ControlEdison
 @date $Date$


"""
import sys
import time
sys.path.append(".")
import os

import rtctree.tree

# Import RTM module
import RTC
import OpenRTM_aist




# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
controledison_spec = ["implementation_id", "ControlEdison", 
		 "type_name",         "ControlEdison", 
		 "description",       "ControlEdison", 
		 "version",           "1.0.0", 
		 "vendor",            "Miyamoto Nobuhiko", 
		 "category",          "TES", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

class StateChangeTask(OpenRTM_aist.Task):
        def __init__(self, funcName, comps):
                OpenRTM_aist.Task.__init__(self)
                self.funcName = funcName
                self.comps = comps

        def svc(self):
                for c in self.comps:
                        func = getattr(c, self.funcName ,None)
                        func(0)
        

##
# @class ControlEdison
# @brief ControlEdison
# 
# 
class ControlEdison(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
        def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
		



		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>

        def getNode(self, node, cl):
                values = node._children.values()
                for v in values:
                        if v.is_component:
                                cl.append(v)
                    
                        elif v.is_manager:
                                pass
                        else:
                                
                                self.getNode(v, cl)

        def getCompList(self):
                tree = rtctree.tree.RTCTree(servers='localhost', orb=self._manager.getORB())
                node = tree._root
                compList = []
                self.getNode(node, compList)

                return compList

		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The shutdown action when ExecutionContext stop
		# former rtc_stopping_entry()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onShutdown(self, ec_id):
                compList = self.getCompList()
                for c in compList:
                        c.exit()
                
		return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
                m_task_s = StateChangeTask("activate_in_ec", self.getCompList())
                """compList = self.getCompList()
                for c in compList:
                        c.activate_in_ec(0)"""
                m_task_s.activate()
                        
                
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
                m_task_s = StateChangeTask("deactivate_in_ec", self.getCompList())

                """compList = self.getCompList()
                for c in compList:
                        c.deactivate_in_ec(0)"""

                m_task_s.activate()
                
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The execution action that is invoked periodically
	#	# former rtc_active_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onExecute(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The reset action that is invoked resetting
		# This is same but different the former rtc_init_entry()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onReset(self, ec_id):
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def ControlEdisonInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=controledison_spec)
    manager.registerFactory(profile,
                            ControlEdison,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ControlEdisonInit(manager)

    # Create a component
    comp = manager.createComponent("ControlEdison")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()
	os.system("shutdown -h now")
	

