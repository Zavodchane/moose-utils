import os

import cv2

from trash import not_olenies_files, not_kosuls_files, not_kabargas_files

BASE_DIR: str = os.getcwd()
PHOTOS_DIRS: dict = {
    "Кабарга": not_kabargas_files,
    "Косуля": not_kosuls_files,
    "Олень": not_olenies_files,
}
OLEN_VIDEOS: list = [
    "DSC_5201.MOV",
    "DSC_5212.MOV",
]


def delete(dir: str, file: str):
    try:
        os.remove(os.path.join(BASE_DIR, dir, file))
        print(f"{BASE_DIR}\\{dir}\\{file} - DELETED")
    except FileNotFoundError:
        pass
    except OSError:
        pass


def delete_unnecessary_photos():
    for dir in PHOTOS_DIRS.keys():
        for file in PHOTOS_DIRS[dir]:
            delete(dir=dir, file=file)
        print(f"{BASE_DIR}\\{dir} - DONE")


def video_to_frames(video_path: str):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Ошибка: Не удалось открыть видео файл {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = f"{video_path[70:].replace('.', '_')}_{frame_count}.png"
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

        if not os.path.isfile(frame_filename):
            print(f"Ошибка: Не удалось сохранить кадр {frame_filename}")

    cap.release()
    print("Разбиение видео на кадры завершено.")


def create_photos_from_videos():
    for video_file in OLEN_VIDEOS:
        video_path = os.path.join(BASE_DIR, "Олень", video_file)
        print(f"Обработка видео: {video_path}")
        video_to_frames(video_path=video_path)


def main():
    create_photos_from_videos()
    delete_unnecessary_photos()


if __name__ == "__main__":
    main()
