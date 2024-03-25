import cv2 as cv

# img = cv.imread("Photos/cat.jpg")

# cv.imshow("CAT", img)

# cv.waitKey(0)

#---------------------------------------------------------------------------------

# Reading Videos

capture = cv.VideoCapture("Videos/dog.mp4")

while True:

    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow("Video", frame)
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    else:
        break

    """
    This ord() function converts the character "a" to its corresponding Unicode keycode, 
    and then it can be compared with the keycode returned by cv.waitKey().
    """

capture.release()
cv.destroyAllWindows()

"""
isTrue, frame = capture.read(): capture.read() yöntemi, bir sonraki kareyi okur ve frame adlı değişkene atar. 
isTrue ise, kare başarıyla okunduğunu gösteren bir boolean değerdir. Eğer isTrue False ise, video dosyasının sonuna gelinmiş demektir
ve döngüden çıkılır.

cv.imshow("Video Of Dog", frame): cv.imshow() yöntemi, bir pencerede bir görüntüyü göstermek için kullanılır. 
Bu satır, "Video Of Dog" adlı bir pencere oluşturur ve frame değişkenindeki kareyi bu pencerede gösterir.

if cv.waitKey(20) & 0xFF == "d":: Bu satır, bir tuşa basılıp basılmadığını kontrol eder. cv.waitKey(20) yöntemi, 
her frame sonrası 20 milisaniye boyunca bir tuşa basılmayı bekler. Eğer kullanıcı "d" tuşuna basarsa (0xFF == "d"), döngüden çıkılır.

capture.release(): VideoCapture nesnesini serbest bırakır. 
Bu, video dosyasını işlemeyi bitirdiğimizde kaynakları serbest bırakmak için önemlidir.

cv.destroyAllWindows(): Tüm OpenCV pencerelerini kapatır. Bu, programı sonlandırdığımızda tüm pencerelerin kapatılmasını sağlar.
"""