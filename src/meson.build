pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'fitness')
gnome = import('gnome')

gnome.compile_resources('fitness',
  'fitness.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'fitness.in',
  output: 'fitness',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

fitness_sources = [
  '__init__.py',
  'activity.py',
  'activity_row.py',
  'history.py',
  'main.py',
  'record_activity_dialog.py',
  'window.py',
]

install_data(fitness_sources, install_dir: moduledir)
