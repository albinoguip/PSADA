from Modules.UIFunctions.DYN_Functions import *


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


        # widgets.dynamic_read_file_button.clicked.connect(lambda: DYN_Functions.dvp_read_file_button_function(app))

        # widgets.dynamic_vars_search.clicked.connect(lambda: DYN_Functions.processed_open_button_function(app))
        # widgets.dynamic_instavel.clicked.connect(lambda: DYN_Functions.instavel_button(app))
        # widgets.dynamic_estavel.clicked.connect(lambda: DYN_Functions.estavel_button(app))
        # widgets.dynamic_per_cont.clicked.connect(lambda: DYN_Functions.per_cont_button(app))
        # widgets.dynamic_per_group.clicked.connect(lambda: DYN_Functions.per_group_button(app))
        # widgets.dynamic_plot_button.clicked.connect(lambda: DYN_Functions.dynamic_plot_function(app)) 