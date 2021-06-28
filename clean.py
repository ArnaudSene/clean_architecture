"""Init script to create a Clean Architecrure environment."""

import os
import argparse


# CLEAN_FEAT_STRUCTURE = ['domains', 'applications', 'interfaces', 'providers']
TEST_ENV = {
    'path': {'root': 'tests', 'subs': ['unit', 'functional']}

}
CLEAN_FEAT_STRUCTURE = {
    'root_path': {
        'init': {
            'docstring': '"""This is the init for __ROOT__."""',
        },
    },
    'structure': {
        'domains': {
            'docstring': '"""This is the domain (entity, DTO} for __FEAT__."""',
        },
        'applications': {
            'docstring': '"""This is the application (use case} for '
                         '__FEAT__."""',
        },
        'interfaces': {
            'docstring': '"""This is the interface (abstract) for __FEAT__."""',
        },
        'providers': {
            'docstring': '"""This is the provider for __FEAT__."""',
        },
    },
    'tests': {
        'name': 'tests',
        'unit': {
            'name': 'unit',
            'domains': {
                'docstring': '"""This is the domain (entity, DTO} unit test '
                             'for __FEAT__."""',
            },
            'applications': {
                'docstring': '"""This is the application (use case} unit test '
                             'for __FEAT__."""',
            },
            'interfaces': {
                'docstring': '"""This is the interface (abstract) unit test '
                             'for __FEAT__."""',
            },
            'providers': {
                'docstring': '"""This is the provider unit test for '
                             '__FEAT__."""',
            },
        },
        'functional': {
            'name': 'functional',
            'docstring': '"""This is the functional test for __FEAT__."""',
        },
    },
}


def parser():
    """"""
    _parser = argparse.ArgumentParser(
        description='Create a Clean Architecture environment.')
    _parser.add_argument('--root_name', '-r', help='Root folder name')
    _parser.add_argument('--feat_name', '-f', help='Feature name')
    args = _parser.parse_args()

    if not args.root_name or not args.feat_name:
        _parser.print_help()
        raise ValueError("Provide 'root_name' and 'feat_name'")
    
    return args


def create_docstring(
        file: str,
        docstring: str,
        name: str,
        root_path: bool = False):
    """"""
    print(f'Add docstring in {file}')

    _docstring = docstring.replace('__FEAT__', name)
    if root_path:
        _docstring = docstring.replace('__ROOT__', name)

    with open(file, 'a') as f:
        f.write(_docstring + "\n")


def create_env(root_name: str, feat_name: str):
    """"""
    if not os.path.exists(root_name):
        print(f'Create {root_name}.')
        os.makedirs(root_name)

    init_file = os.path.join(root_name, '__init__.py')
    if not os.path.isfile(init_file):
        print(f'Create {init_file}')
        docstring = CLEAN_FEAT_STRUCTURE['root_path']['init']['docstring']
        create_docstring(
            file=init_file, docstring=docstring, name=feat_name, root_path=True)

    for folder in CLEAN_FEAT_STRUCTURE['structure'].keys():
        docstring = CLEAN_FEAT_STRUCTURE['structure'][folder]['docstring']
        _folder = os.path.join(root_name, folder)

        if not os.path.exists(_folder):
            print(f'Create {_folder}')
            os.makedirs(_folder)

        init_file = os.path.join(_folder, '__init__.py')
        if not os.path.isfile(init_file):
            print(f'Create {init_file}')
            create_docstring(
                file=init_file, docstring=docstring, name=feat_name)

        feat_file = os.path.join(_folder, f'{feat_name}.py')
        if not os.path.isfile(feat_file):
            print(f'Create {feat_file}')
            create_docstring(
                file=feat_file, docstring=docstring, name=feat_name)

    # TESTS
    test_root = os.path.join(root_name, CLEAN_FEAT_STRUCTURE['tests']['name'])
    if not os.path.exists(test_root):
        print(f'Create {test_root}')
        os.makedirs(test_root)

    # Functional test
    test_functional = os.path.join(
        test_root, CLEAN_FEAT_STRUCTURE['tests']['functional']['name'])
    test_functional_docstring = \
        CLEAN_FEAT_STRUCTURE['tests']['functional']['docstring']
    test_functional_file = os.path.join(test_functional, f'test_{feat_name}.py')
    
    if not os.path.exists(test_functional):
        print(f'Create {test_functional}')
        os.makedirs(test_functional)

    if not os.path.isfile(test_functional_file):
        print(f'Create {test_functional_file}')
        create_docstring(
            file=test_functional_file,
            docstring=test_functional_docstring, name=feat_name)

    # Unit test
    test_unit = os.path.join(
        test_root, CLEAN_FEAT_STRUCTURE['tests']['unit']['name'])
    
    if not os.path.exists(test_unit):
        print(f'Create {test_unit}')
        os.makedirs(test_unit)

    for folder in CLEAN_FEAT_STRUCTURE['structure'].keys():
        test_unit_docstring = \
            CLEAN_FEAT_STRUCTURE['tests']['unit'][folder]['docstring']
        test_unit_folder = os.path.join(test_unit, folder)
        test_unit_file = os.path.join(test_unit_folder, f'test_{feat_name}.py')

        if not os.path.exists(test_unit_folder):
            print(f'Create {test_unit_folder}')
            os.makedirs(test_unit_folder)           

        if not os.path.isfile(test_unit_file):
            print(f'Create {test_unit_file}')
            create_docstring(
                file=test_unit_file,
                docstring=test_unit_docstring, name=feat_name)

    print(f'Clean architecture environment set for {root_name} '
          f'feature: {feat_name}')


def main():
    """"""
    try:
        args = parser()
        create_env(root_name=args.root_name, feat_name=args.feat_name)
    except ValueError as exc:
        print(f'{exc}')


if __name__ == '__main__':
    main()
