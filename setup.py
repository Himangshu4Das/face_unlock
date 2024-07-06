setup(
    name="face_unlock",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "dlib",
        "face_recognition",
        "python-pam",
    ],
    entry_points={
        "console_scripts": [
            "face-unlock-capture=face_unlock.capture_face:capture_face",
        ],
    },
    data_files=[
        ("/lib/security", ["face_unlock/pam_face_recognition.py"]),
    ],
    include_package_data=True,
    zip_safe=False,
)
