# Install all SVG icons from hicolor/scalable/apps so builds don't break
# when filenames differ (AppID vs author-provided names).

icons = files('hicolor/scalable/apps/*.svg')

if icons == []
  error('No SVG icons found in hicolor/scalable/apps. Ensure SVGs are present (for example org.nexuspenn.nexaos.customize.svg) or update meson.build to point to the correct path.')
endif

install_data(icons,
  install_dir: join_paths(get_option('datadir'), 'icons', 'hicolor', 'scalable', 'apps')
)
