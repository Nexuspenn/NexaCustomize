application_id = 'org.nexuspenn.nexaos.customize'

# Install scalable app icon
scalable_dir = join_paths('hicolor', 'scalable', 'apps')
install_data(
  join_paths(scalable_dir, '@0@.svg'.format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

# Install the symbolic app icon
symbolic_dir = join_paths('hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, '@0@-symbolic.svg'.format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)

# Additional symbolic assets
symbolic_install_dir = join_paths(get_option('datadir'), 'icons', 'hicolor', 'symbolic', 'apps')
install_data('theming-symbolic.svg', install_dir: symbolic_install_dir)
install_data('layout-symbolic.svg', install_dir: symbolic_install_dir)
install_data('top_bar_with_menu.svg', install_dir: symbolic_install_dir)
install_data('bottom_panel.svg', install_dir: symbolic_install_dir)
install_data('gnome-layout.svg', install_dir: symbolic_install_dir)
install_data('top_bar_dock.svg', install_dir: symbolic_install_dir)
install_data('top_bar_menu_dock.svg', install_dir: symbolic_install_dir)
install_data('top_bar_left_dock.svg', install_dir: symbolic_install_dir)
