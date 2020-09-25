import unreal
import imgspc
import importer, exporter, utilities

# Add new toolbar button with logo
imgspc.make_menu_item(menu_path='ImgSpc', icon_path='MyPlugin/Resources/imgspc-logo-large.png', tooltip='Open the Imaginary Spaces Menu')

# Create Import & Export menu-items
imgspc.make_menu_item(menu_path='ImgSpc/Import...', callback='importer.import_file()', tooltip='Import file')
imgspc.make_menu_item(menu_path='ImgSpc/Export...', callback='exporter.export_file(".gltf")', tooltip='Export file')

# Create Help sub-menu and add About menu-item
imgspc.make_menu_item(
    menu_path='ImgSpc/Help/About Imaginary Spaces', 
    callback='utilities.load_docs()', 
    icon_path='MyPlugin/Resources/imgspc-logo-large.png', 
    tooltip='About Imaginary Spaces'
)

# Add to the Main Menu bar
imgspc.make_menu_item('LevelEditor.MainMenu/ImgSpc')
imgspc.make_menu_item('LevelEditor.MainMenu/ImgSpc/Import...', callback='importer.import_file()', tooltip='Import file')
imgspc.make_menu_item('LevelEditor.MainMenu/ImgSpc/Export...', callback='exporter.export_file(".gltf")', tooltip='Export file')
imgspc.make_menu_item(
    'LevelEditor.MainMenu/ImgSpc/Help/About Imaginary Spaces',
    callback='utilities.load_docs()',
    icon_path='MyPlugin/Resources/imgspc-logo-large.png',
    tooltip='About Imaginary Spaces'
)