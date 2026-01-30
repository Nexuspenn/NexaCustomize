application_id = 'org.nexuspenn.nexaos.customize'

# Install scalable icons. Prefer any SVGs present, fallback to the AppID-named file.
scalable_dir = join_paths('hicolor', 'scalable', 'apps')
scalable_icons = files(join_paths(scalable_dir, '*.svg'))

if scalable_icons == []
  # Fallback to the AppID-specific filename for compatibility with older setups.
  scalable_icons = files(join_paths(scalable_dir, ('@0@.svg').format(application_id)))
  if scalable_icons == []
    error('No SVG icons found in hicolor/scalable/apps. Ensure SVGs are present or update meson.build')
  endif
endif

install_data(scalable_icons,
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

# Install the symbolic app icon (AppID-specific)
symbolic_dir = join_paths('hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, ('@0@-symbolic.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)

# Additional symbolic assets installed to the system icons directory
symbolic_install_dir = join_paths(get_option('datadir'), 'icons', 'hicolor', 'symbolic', 'apps')

install_data('theming-symbolic.svg', install_dir: symbolic_install_dir)
install_data('layout-symbolic.svg', install_dir: symbolic_install_dir)
install_data('top_bar_with_menu.svg', install_dir: symbolic_install_dir)
install_data('bottom_panel.svg', install_dir: symbolic_install_dir)
install_data('gnome-layout.svg', install_dir: symbolic_install_dir)
install_data('top_bar_dock.svg', install_dir: symbolic_install_dir)
install_data('top_bar_menu_dock.svg', install_dir: symbolic_install_dir)
install_data('top_bar_left_dock.svg', install_dir: symbolic_install_dir)
