from PyQt5.QtWidgets import *
from krita import *
from functools import partial


class QuickBrushSettings(DockWidget):

	def __init__(self):
		super().__init__()

		#TODO: your config here

		brush_sizes = [5, 10, 15, 20, 30]
		brush_opacity_settings = [100, 80, 50]

		#TODO: end config

		self.setWindowTitle("Quick Brush Settings")

		mainWidget = QWidget(self)
		self.setWidget(mainWidget)

		setttabs = QTabWidget(mainWidget)
		tab_size = QWidget(self)
		tab_opacity = QWidget(self)

		setttabs.addTab(tab_size, "Brush Size")
		setttabs.addTab(tab_opacity, "Opacity")

		tab_size.layout = QGridLayout(self)
		## array
		for brush_size in brush_sizes:
			radio_button = QRadioButton()
			radio_button.setText(f"{brush_size}px")
			radio_button.clicked.connect(partial(self.setBrushSize, brush_size))
			tab_size.layout.addWidget(radio_button)

		tab_size.setLayout(tab_size.layout)

		tab_opacity.layout = QVBoxLayout(self)
		for brush_opacity in brush_opacity_settings:
			radio_button = QRadioButton()
			radio_button.setText(f"{brush_opacity}%")
			radio_button.clicked.connect(
			    partial(self.setBrushOpacity, brush_opacity))
			tab_opacity.layout.addWidget(radio_button)
		tab_opacity.setLayout(tab_opacity.layout)

		mainWidget.setLayout(QVBoxLayout())
		mainWidget.layout().addWidget(setttabs)

	def canvasChanged(self, canvas):
		pass

	def setBrushSize(self, pbrush_size):
		Krita.instance().activeWindow().activeView().setBrushSize(pbrush_size)

	def setBrushOpacity(self, pbrush_opacity):
		Krita.instance().activeWindow().activeView().setPaintingOpacity(
		    pbrush_opacity / 100)


Krita.instance().addDockWidgetFactory(
    DockWidgetFactory("quickbrushsettings", DockWidgetFactoryBase.DockRight,
                      QuickBrushSettings))
