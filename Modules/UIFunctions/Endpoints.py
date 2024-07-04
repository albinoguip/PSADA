from Modules.UIFunctions.DYN_Functions import *
from Modules.UIFunctions.NET_Functions import *
from Modules.UIFunctions.STA_Functions import *
from Modules.UIFunctions.STD_Functions import *


class connect():

    def __init__(self):

        pass

    def dyn_conn(self, widgets, app):

        widgets.DYNAMIC_search_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_search_button_FUNCTION(app))
        widgets.DYNAMIC_read_file_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_read_file_button_FUNCTION(app))

        widgets.DYNAMIC_vars_search.clicked.connect(lambda: DYN_Functions.DYNAMIC_vars_search_FUNCTION(app))
        widgets.DYNAMIC_read_vars_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_read_vars_button_FUNCTION(app))

        widgets.DYNAMIC_plot_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_plot_button_FUNCTION(app))
        widgets.DYNAMIC_button_apply_filter.clicked.connect(lambda: DYN_Functions.DYNAMIC_button_apply_filter_FUNCTION(app))
        widgets.DYNAMIC_button_remove_filter.clicked.connect(lambda: DYN_Functions.DYNAMIC_plot_button_FUNCTION(app))


        widgets.DYNAMIC_add_section_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_add_section_button_FUNCTION(app))
        widgets.DYNAMIC_add_plot_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_add_plot_button_FUNCTION(app))
        widgets.DYNAMIC_select_section.currentTextChanged.connect(lambda: DYN_Functions.DYNAMIC_select_section_FUNCTION(app))

        widgets.DYNAMIC_add_to_json_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_add_to_json_button_FUNCTION(app))
        widgets.DYNAMIC_page_to_plot_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_page_to_plot_button_FUNCTION(app))
        widgets.DYNAMIC_save_json_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_save_json_button_FUNCTION(app))


        widgets.DYNAMIC_search_json_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_search_json_button_FUNCTION(app))
        widgets.DYNAMIC_read_json_button.clicked.connect(lambda: DYN_Functions.DYNAMIC_read_json_button_FUNCTION(app))


        widgets.run_DYNAMIC.clicked.connect(lambda: DYN_Functions.run_DYNAMIC_FUNCTION(app))
        widgets.actionSave_DYNAMIC.clicked.connect(lambda: DYN_Functions.actionSave_DYNAMIC_FUNCTION(app))
        widgets.actionZoom_In_DYNAMIC.clicked.connect(lambda: DYN_Functions.actionZoom_In_DYNAMIC_FUNCTION(app))
        widgets.actionZoom_Out_DYNAMIC.clicked.connect(lambda: DYN_Functions.actionZoom_Out_DYNAMIC_FUNCTION(app))
        widgets.actionPage_down_DYNAMIC.clicked.connect(lambda: DYN_Functions.actionPage_down_DYNAMIC_FUNCTION(app))
        widgets.actionPage_up_DYNAMIC.clicked.connect(lambda: DYN_Functions.actionPage_up_DYNAMIC_FUNCTION(app))



    def net_conn(self, widgets, app):

        widgets.NETWORK_search_button.clicked.connect(lambda: NET_Functions.NETWORK_search_button_FUNCTION(app))
        widgets.NETWORK_read_file_button.clicked.connect(lambda: NET_Functions.NETWORK_read_file_button_FUNCTION(app))

        widgets.NETWORK_vars_search.clicked.connect(lambda: NET_Functions.NETWORK_vars_search_FUNCTION(app))
        widgets.NETWORK_read_vars_button.clicked.connect(lambda: NET_Functions.NETWORK_read_vars_button_FUNCTION(app))

        widgets.NETWORK_plot_button.clicked.connect(lambda: NET_Functions.NETWORK_plot_button_FUNCTION(app))
        widgets.NETWORK_button_apply_filter.clicked.connect(lambda: NET_Functions.NETWORK_button_apply_filter_FUNCTION(app))
        widgets.NETWORK_button_remove_filter.clicked.connect(lambda: NET_Functions.NETWORK_plot_button_FUNCTION(app))


        widgets.NETWORK_add_section_button.clicked.connect(lambda: NET_Functions.NETWORK_add_section_button_FUNCTION(app))
        widgets.NETWORK_add_plot_button.clicked.connect(lambda: NET_Functions.NETWORK_add_plot_button_FUNCTION(app))
        widgets.NETWORK_select_section.currentTextChanged.connect(lambda: NET_Functions.NETWORK_select_section_FUNCTION(app))

        widgets.NETWORK_add_to_json_button.clicked.connect(lambda: NET_Functions.NETWORK_add_to_json_button_FUNCTION(app))
        widgets.NETWORK_page_to_plot_button.clicked.connect(lambda: NET_Functions.NETWORK_page_to_plot_button_FUNCTION(app))
        widgets.NETWORK_save_json_button.clicked.connect(lambda: NET_Functions.NETWORK_save_json_button_FUNCTION(app))


        widgets.NETWORK_search_json_button.clicked.connect(lambda: NET_Functions.NETWORK_search_json_button_FUNCTION(app))
        widgets.NETWORK_read_json_button.clicked.connect(lambda: NET_Functions.NETWORK_read_json_button_FUNCTION(app))


        widgets.run_NETWORK.clicked.connect(lambda: NET_Functions.run_NETWORK_FUNCTION(app))
        widgets.actionSave_NETWORK.clicked.connect(lambda: NET_Functions.actionSave_NETWORK_FUNCTION(app))
        widgets.actionZoom_In_NETWORK.clicked.connect(lambda: NET_Functions.actionZoom_In_NETWORK_FUNCTION(app))
        widgets.actionZoom_Out_NETWORK.clicked.connect(lambda: NET_Functions.actionZoom_Out_NETWORK_FUNCTION(app))
        widgets.actionPage_down_NETWORK.clicked.connect(lambda: NET_Functions.actionPage_down_NETWORK_FUNCTION(app))
        widgets.actionPage_up_NETWORK.clicked.connect(lambda: NET_Functions.actionPage_up_NETWORK_FUNCTION(app))


    def sta_conn(self, widgets, app):

        widgets.STATIC_search_button.clicked.connect(lambda: STA_Functions.STATIC_search_button_FUNCTION(app))
        widgets.STATIC_read_file_button.clicked.connect(lambda: STA_Functions.STATIC_read_file_button_FUNCTION(app))

        widgets.STATIC_vars_search.clicked.connect(lambda: STA_Functions.STATIC_vars_search_FUNCTION(app))
        widgets.STATIC_read_vars_button.clicked.connect(lambda: STA_Functions.STATIC_read_vars_button_FUNCTION(app))

        widgets.STATIC_plot_button.clicked.connect(lambda: STA_Functions.STATIC_plot_button_FUNCTION(app))
        # widgets.STATIC_button_apply_filter.clicked.connect(lambda: STA_Functions.STATIC_button_apply_filter_FUNCTION(app))
        # widgets.STATIC_button_remove_filter.clicked.connect(lambda: STA_Functions.STATIC_plot_button_FUNCTION(app))


        # widgets.STATIC_add_section_button.clicked.connect(lambda: STA_Functions.STATIC_add_section_button_FUNCTION(app))
        # widgets.STATIC_add_plot_button.clicked.connect(lambda: STA_Functions.STATIC_add_plot_button_FUNCTION(app))
        # widgets.STATIC_select_section.currentTextChanged.connect(lambda: STA_Functions.STATIC_select_section_FUNCTION(app))

        # widgets.STATIC_add_to_json_button.clicked.connect(lambda: STA_Functions.STATIC_add_to_json_button_FUNCTION(app))
        # widgets.STATIC_page_to_plot_button.clicked.connect(lambda: STA_Functions.STATIC_page_to_plot_button_FUNCTION(app))
        # widgets.STATIC_save_json_button.clicked.connect(lambda: STA_Functions.STATIC_save_json_button_FUNCTION(app))


        # widgets.STATIC_search_json_button.clicked.connect(lambda: STA_Functions.STATIC_search_json_button_FUNCTION(app))
        # widgets.STATIC_read_json_button.clicked.connect(lambda: STA_Functions.STATIC_read_json_button_FUNCTION(app))


        # widgets.run_STATIC.clicked.connect(lambda: STA_Functions.run_STATIC_FUNCTION(app))
        # widgets.actionSave_STATIC.clicked.connect(lambda: STA_Functions.actionSave_STATIC_FUNCTION(app))
        # widgets.actionZoom_In_STATIC.clicked.connect(lambda: STA_Functions.actionZoom_In_STATIC_FUNCTION(app))
        # widgets.actionZoom_Out_STATIC.clicked.connect(lambda: STA_Functions.actionZoom_Out_STATIC_FUNCTION(app))
        # widgets.actionPage_down_STATIC.clicked.connect(lambda: STA_Functions.actionPage_down_STATIC_FUNCTION(app))
        # widgets.actionPage_up_STATIC.clicked.connect(lambda: STA_Functions.actionPage_up_STATIC_FUNCTION(app))




    def std_conn(self, widgets, app):

        widgets.STADYN_search_button.clicked.connect(lambda: STD_Functions.STADYN_search_button_FUNCTION(app))
        widgets.STADYN_read_file_button.clicked.connect(lambda: STD_Functions.STADYN_read_file_button_FUNCTION(app))

        widgets.STADYN_vars_search.clicked.connect(lambda: STD_Functions.STADYN_vars_search_FUNCTION(app))
        widgets.STADYN_read_vars_button.clicked.connect(lambda: STD_Functions.STADYN_read_vars_button_FUNCTION(app))

        widgets.STADYN_plot_button.clicked.connect(lambda: STD_Functions.STADYN_plot_button_FUNCTION(app))
        widgets.STADYN_button_apply_filter.clicked.connect(lambda: STD_Functions.STADYN_button_apply_filter_FUNCTION(app))
        widgets.STADYN_button_remove_filter.clicked.connect(lambda: STD_Functions.STADYN_plot_button_FUNCTION(app))


        widgets.STADYN_add_section_button.clicked.connect(lambda: STD_Functions.STADYN_add_section_button_FUNCTION(app))
        widgets.STADYN_add_plot_button.clicked.connect(lambda: STD_Functions.STADYN_add_plot_button_FUNCTION(app))
        widgets.STADYN_select_section.currentTextChanged.connect(lambda: STD_Functions.STADYN_select_section_FUNCTION(app))

        widgets.STADYN_add_to_json_button.clicked.connect(lambda: STD_Functions.STADYN_add_to_json_button_FUNCTION(app))
        widgets.STADYN_page_to_plot_button.clicked.connect(lambda: STD_Functions.STADYN_page_to_plot_button_FUNCTION(app))
        widgets.STADYN_save_json_button.clicked.connect(lambda: STD_Functions.STADYN_save_json_button_FUNCTION(app))


        widgets.STADYN_search_json_button.clicked.connect(lambda: STD_Functions.STADYN_search_json_button_FUNCTION(app))
        widgets.STADYN_read_json_button.clicked.connect(lambda: STD_Functions.STADYN_read_json_button_FUNCTION(app))


        widgets.run_STADYN.clicked.connect(lambda: STD_Functions.run_STADYN_FUNCTION(app))
        widgets.actionSave_STADYN.clicked.connect(lambda: STD_Functions.actionSave_STADYN_FUNCTION(app))
        widgets.actionZoom_In_STADYN.clicked.connect(lambda: STD_Functions.actionZoom_In_STADYN_FUNCTION(app))
        widgets.actionZoom_Out_STADYN.clicked.connect(lambda: STD_Functions.actionZoom_Out_STADYN_FUNCTION(app))
        widgets.actionPage_down_STADYN.clicked.connect(lambda: STD_Functions.actionPage_down_STADYN_FUNCTION(app))
        widgets.actionPage_up_STADYN.clicked.connect(lambda: STD_Functions.actionPage_up_STADYN_FUNCTION(app))