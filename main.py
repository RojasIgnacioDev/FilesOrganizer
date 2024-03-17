import core

def main():
    core.sort_files(core.images_folder, core.image_extensions)
    core.sort_files(core.documents_folder, core.document_extensions)

if __name__ == "__main__":
    main()