import face_recognition

hayk_image = face_recognition.load_image_file("hayk1.jpg")
gates_image = face_recognition.load_image_file("gates.jpg")
zuck_image = face_recognition.load_image_file("zuck.jpg")

unknown_image = face_recognition.load_image_file("hayk2.jpg")


try:
    hayk_face_encoding = face_recognition.face_encodings(hayk_image)[0]
    gates_face_encoding = face_recognition.face_encodings(gates_image)[0]
    zuck_face_encoding = face_recognition.face_encodings(zuck_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("Нэма тут лиц :/")
    quit()

known_faces = [
    hayk_face_encoding,
    gates_face_encoding,
    zuck_face_encoding
]


results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print(f"Это Гайк? {results[0]}")
print(f"Это Билл Гейтс? {results[1]}")
print(f"Это Марк Цукерберг?{results[2]}")
print(f"Это какой-то ноунейм? {not True in results}")
