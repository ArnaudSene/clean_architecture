"""Init script to create a Clean Architecrure environment."""

import os
import argparse


CLEAN_FEAT_STRUCTURE = ['domains', 'applications', 'interfaces', 'providers']
TEST_ENV = {
    'path': { 'root': 'tests', 'subs': ['unit', 'functional']}

}
CLEAN_FEAT_STRUCTURE = {
    'structure': {
        'domains': {
            'docstring': '"""This is the domain (entity, DTO} for __FEAT__."""'
        },
        'applications': {
            'docstring': '"""This is the application (use case} for __FEAT__."""'
        },
        'interfaces': {
            'docstring': '"""This is the interface (abstract) for __FEAT__."""'
        },
        'providers': {
            'docstring': '"""This is the provider for __FEAT__."""'
        },
    },
    'tests': {
        'name': 'tests',
        'unit': {
            'name': 'unit',
            'domains': {
                'docstring': '"""This is the domain (entity, DTO} unit test for __FEAT__."""'
            },
            'applications': {
                'docstring': '"""This is the application (use case} unit test for __FEAT__."""'
            },
            'interfaces': {
                'docstring': '"""This is the interface (abstract) unit test for __FEAT__."""'
            },
            'providers': {
                'docstring': '"""This is the provider unit test for __FEAT__."""'
            },
        },
        'functional': {
            'name': 'functional',
            'docstring': '"""This is the functional test for __FEAT__."""'
        },
    },
}

def parser():
    """"""
    parser = argparse.ArgumentParser(
        description='Create a Clean Architecture environment.')
    parser.add_argument('--root', '-r', help='Root folder name')
    parser.add_argument('--feat', '-f', help='Feature name')
    args = parser.parse_args()

    if not args.root or not args.feat:
        parser.print_help()
    
    return args

def create_docstring(file: str, docstring: str, feat: str):
    """"""
    print(f'Add docstring in {file}')
    
    _docstring = docstring.replace('__FEAT__', feat)

    with open(file, 'a') as f:
        f.write(_docstring)

def create_env(root: str, feat: str):
    """"""
    if not os.path.exists(root):
        print(f'Create {root}.')
        os.makedirs(root)

    for folder in CLEAN_FEAT_STRUCTURE['structure'].keys():
        docstring = CLEAN_FEAT_STRUCTURE['structure'][folder]['docstring']
        _folder = os.path.join(root, folder)

        if not os.path.exists(_folder):
            print(f'Create {_folder}')
            os.makedirs(_folder)

        init_file = os.path.join(_folder, '__init__.py')
        if not os.path.isfile(init_file):
            print(f'Create {init_file}')
            create_docstring(file=init_file, docstring=docstring, feat=feat)

        feat_file = os.path.join(_folder, f'{feat}.py')
        if not os.path.isfile(feat_file):
            print(f'Create {feat_file}')
            create_docstring(file=feat_file, docstring=docstring, feat=feat)

    # TESTS
    test_root = os.path.join(root, CLEAN_FEAT_STRUCTURE['tests']['name'])
    if not os.path.exists(test_root):
        print(f'Create {test_root}')
        os.makedirs(test_root)

    # Functional test
    test_functional = os.path.join(test_root, CLEAN_FEAT_STRUCTURE['tests']['functional']['name'])
    test_functional_docstring = CLEAN_FEAT_STRUCTURE['tests']['functional']['docstring']
    test_functional_file = os.path.join(test_functional, f'test_{feat}.py')
    
    if not os.path.exists(test_functional):
        print(f'Create {test_functional}')
        os.makedirs(test_functional)

    if not os.path.isfile(test_functional_file):
        print(f'Create {test_functional_file}')
        create_docstring(file=test_functional_file, docstring=test_functional_docstring, feat=feat)

    # Unit test
    test_unit = os.path.join(test_root, CLEAN_FEAT_STRUCTURE['tests']['unit']['name'])
    
    if not os.path.exists(test_unit):
        print(f'Create {test_unit}')
        os.makedirs(test_unit)


    for folder in CLEAN_FEAT_STRUCTURE['structure'].keys():
        test_unit_docstring = CLEAN_FEAT_STRUCTURE['tests']['unit'][folder]['docstring']
        test_unit_folder = os.path.join(test_unit, folder)
        test_unit_file = os.path.join(test_unit_folder, f'test_{feat}.py')

        if not os.path.exists(test_unit_folder):
            print(f'Create {test_unit_folder}')
            os.makedirs(test_unit_folder)           

            if not os.path.isfile(test_unit_file):
                print(f'Create {test_unit_file}')
                create_docstring(file=test_unit_file, docstring=test_unit_docstring, feat=feat)
        

    print(f'Clean architecture environment set for {root} feature: {feat}')

def main():
    """"""
    args = parser()
    create_env(root=args.root, feat=args.feat)


if __name__ == '__main__':
    main()
