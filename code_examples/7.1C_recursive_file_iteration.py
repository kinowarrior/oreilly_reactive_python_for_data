import os

from rx import Observable


def recursive_files_in_directory(folder):

    def emit_files_recursively(observer):
        for root, directories, filenames in os.walk(folder):
            for directory in directories:
                observer.on_next(os.path.join(root, directory))

            for filename in filenames:
                observer.on_next(os.path.join(root, filename))

        observer.on_completed()

    return Observable.create(emit_files_recursively)


recursive_files_in_directory('/Users/arcseldon/work/study/python-monopoly/src') \
    .filter(lambda f: f.endswith('.py')) \
    .subscribe(on_next=lambda l: print(l), on_error=lambda e: print(e))
