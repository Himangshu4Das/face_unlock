# Face Unlock

A simple face unlock feature for Linux with a fallback to password authentication.

## Installation

To install the Face Unlock package directly from GitHub, use the following command:

'''sh
pip install git+https://github.com/yourusername/face_unlock.git
'''

## Usage

### 1. Capture Your Face

Run the following command to capture your face and save the encoding:

'''sh
face-unlock-capture
'''

### 2. Integrate with PAM

Edit `/etc/pam.d/common-auth` to include the following line at the top:

'''sh
auth required pam_python.so /lib/security/pam_face_recognition.py
'''

### 3. Test and Log In

Try logging in using face recognition. If face recognition fails, it will fall back to password authentication.

## Important Considerations

- **Security:** Ensure your face recognition system is robust and secure.
- **Privacy:** Handle biometric data responsibly.
- **Fallback Mechanism:** Ensure that the fallback mechanism (password login) is always available in case face recognition fails.

## Development

If you want to contribute to the development of this package, clone the repository and set up your environment:

'''sh
git clone https://github.com/yourusername/face_unlock.git
cd face_unlock
pip install -r requirements.txt
'''

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
