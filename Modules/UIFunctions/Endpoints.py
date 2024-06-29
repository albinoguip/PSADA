from Modules.UIFunctions.DYN_Functions import *


class connect():

    def __init__(self):

        pass

    def dyn_conn(self, widgets, app):

        widgets.dynamic_local_search_button.clicked.connect(lambda: DYN_Functions.data_match_local_search_button_function(app))
        widgets.dynamic_search_file_button.clicked.connect(lambda: DYN_Functions.dvp_sf_button_function(app))
        widgets.dynamic_read_file_button.clicked.connect(lambda: DYN_Functions.dvp_read_file_button_function(app))

        widgets.dynamic_vars_search.clicked.connect(lambda: DYN_Functions.processed_open_button_function(app))
        widgets.dynamic_instavel.clicked.connect(lambda: DYN_Functions.instavel_button(app))
        widgets.dynamic_estavel.clicked.connect(lambda: DYN_Functions.estavel_button(app))
        widgets.dynamic_per_cont.clicked.connect(lambda: DYN_Functions.per_cont_button(app))
        widgets.dynamic_per_group.clicked.connect(lambda: DYN_Functions.per_group_button(app))
        widgets.dynamic_plot_button.clicked.connect(lambda: DYN_Functions.dynamic_plot_function(app))