from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import textwrap

t = Path("data/times-new-roman.ttf")

t2 = Path("data/Times new roman bold.ttf")

t3 = Path("data/times-new-roman-cyr-kursywa.ttf")

pdfmetrics.registerFont(TTFont("times-new-roman", t))
pdfmetrics.registerFont(TTFont("Times new roman bold", t2))
pdfmetrics.registerFont(TTFont("times-new-roman-cyr-kursywa", t3))


def make_court_f_119(
    place,
    date,
    recipient,
    address,
    case_number,
    check,
    check2,
    check3,
    check4,
    recipient_name,
    recipient_mobil,
    recipient_address,
    check5,
    check6,
    check7,
    check8,
    hrn,
    hrn2,
    kop,
):
    can = canvas.Canvas("court-f-119.pdf", pagesize=A4)
    can.setFont("Helvetica", 11)
    can.drawString(54, 679, check)
    can.drawString(124, 679, check2)
    can.drawString(232, 679, check3)
    can.drawString(85, 663, check4)
    can.drawString(180, 670, check5)
    can.drawString(180, 655, check6)
    can.drawString(54, 633, check7)
    can.drawString(124, 633, check8)
    can.setFont("Helvetica", 10)
    can.drawString(309, 670, hrn[:7])
    can.drawString(269, 655, hrn2[:6])
    can.drawString(322, 655, kop[:2])
    can.setFont("times-new-roman-cyr-kursywa", 11)
    can.drawString(310, 775, place[:14])
    can.drawString(305, 762, date)

    recipient = recipient.replace("\n", " ")
    if recipient:
        lines = textwrap.wrap(recipient, width=46)
        first_line = lines[0]
        remainder = " ".join(lines[1:])

        lines = textwrap.wrap(remainder, 62)
        lines = lines[:1]  # max lines, not including the first.

        can.drawString(133, 743, first_line)
        for n, l in enumerate(lines, 1):
            can.drawString(38, 728 - n, l)

    address = address.replace("\n", " ")
    if address:
        lines = textwrap.wrap(address, width=55)
        first_line = lines[0]
        remainder = " ".join(lines[1:])

        lines = textwrap.wrap(remainder, 62)
        lines = lines[:1]  # max lines, not including the first.

        can.drawString(104, 713, first_line)
        for n, l in enumerate(lines, 1):
            can.drawString(38, 699 - n, l)

    case_number = case_number.replace("\n", " ")
    if case_number:
        lines = textwrap.wrap(case_number, width=25)
        first_line = lines[0]
        remainder = " ".join(lines[1:])

        lines = textwrap.wrap(remainder, 25)
        lines = lines[:4]  # max lines, not including the first.

        can.drawString(405, 775, first_line)
        for n, l in enumerate(lines, 1):
            can.drawString(405, 773 - (n * 15), l)

    can.setFont("times-new-roman-cyr-kursywa", 10)
    recipient_name = recipient_name
    if recipient_name:
        lines = textwrap.wrap(recipient_name, width=15)
        first_line = lines[0]
        remainder = " ".join(lines[1:])

        lines = textwrap.wrap(remainder, 34)
        lines = lines[:1]  # max lines, not including the first.

        can.drawString(512, 678, first_line)
        for n, l in enumerate(lines, 1):
            can.drawString(407, 664 - (n * 1), l)

    can.drawString(468, 650, recipient_mobil[:21])

    recipient_address = recipient_address
    if recipient_address:
        lines = textwrap.wrap(recipient_address, width=25)
        first_line = lines[0]
        remainder = " ".join(lines[1:])

        lines = textwrap.wrap(remainder, 34)
        lines = lines[:2]  # max lines, not including the first.

        can.drawString(469, 637, first_line)
        for n, l in enumerate(lines, 1):
            can.drawString(405, 639 - (n * 15), l)

    can.setFont("Times new roman bold", 11)
    can.drawString(247, 804, "Рекомендоване повідомлення про вручення про поштового")
    can.drawString(278, 793, "відправлення, виплату поштового переказу")
    can.setFont("times-new-roman", 11)
    can.drawString(402, 696, "Підлягає поверненню")
    can.setFont("Times new roman bold", 9)
    can.drawString(52, 688, "Вид та категорія поштового відправлення")
    can.drawString(
        45, 617, "Заповнюється в об'єкті поштового звя'язку місця призначення"
    )
    can.drawString(399, 593, "Обведене жирною лінією заповнює відправник")
    can.setFont("times-new-roman", 9)
    can.drawString(527, 795, "Форма № 119")
    can.drawString(248, 775, "Місце подання")
    can.drawString(248, 762, "Дата подання")
    can.drawString(38, 741, "Найменування адресату")
    can.drawString(38, 712, "Поштова адреса")
    can.drawString(404, 676, "Найменування відправника")
    can.drawString(405, 649, "номер телефону")
    can.drawString(405, 637, "поштова адреса")
    can.drawString(65, 678, "Лист")
    can.drawString(136, 678, "Бандероль")
    can.drawString(245, 678, "Посилка")
    can.drawString(195, 669, "З оголошеною цінністю на                        грн.")
    can.drawString(99, 662, "Рекомендоване")
    can.drawString(195, 654, "Сума післяплати                   грн.         коп.")
    can.drawString(65, 631, "Простий")
    can.drawString(136, 631, "Електронний")
    can.drawString(50, 589, "вручено")
    can.drawString(50, 578, "особисто")
    can.drawString(50, 567, "за довіреністю")
    can.drawString(50, 554, "уповноваженному")
    can.drawString(40, 540, "Розписка в одержанні*")
    can.drawString(179, 581, "(дата)")
    can.drawString(228, 596, "не вручено")
    can.drawString(228, 576, "відмови адресата від одержання")
    can.drawString(228, 565, "закінчення терміну зберігання")
    can.drawString(228, 554, "неправильно зазначена або відсутня адреса")
    can.drawString(228, 541, "інші причини")
    can.drawString(40, 517, "Підпис працівника поштового зв'язку")
    can.setFont("times-new-roman", 8)
    can.drawString(45, 780, "№")
    can.drawString(50, 771, "поштового відправлення, поштового переказу")
    can.drawString(80, 606, "Вищезазначене поштове відправлення, поштовий переказ")
    can.drawString(312, 596, "не виплачено")
    can.drawString(270, 589, "з причини")
    can.drawString(108, 590, "виплачено")
    can.drawString(445, 560, "№")
    can.drawString(460, 550, "повідомлення про вручення")
    can.drawString(
        41,
        501,
        "* Для відправленнь з відміткою  'Судова повістка' - особисто одержувачем або уповноваженою ним "
        "особою учиняється підпис та зазначаєся прізвище.",
    )
    can.setFont("times-new-roman", 7)
    can.drawString(528, 746, "(відбиток календ")
    can.drawString(528, 740, "арного штемпеля)")
    can.drawString(
        20,
        494,
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
        "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _",
    )
    can.setLineWidth(2)
    can.line(
        34, 755, 246, 755
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        246, 787, 246, 754
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    # основа відправлення
    # місце подання і дата подання
    can.line(
        245, 786, 395, 786
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        395, 787, 395, 626
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    # основа відправлення
    can.line(
        34, 626, 396, 626
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        35, 756, 35, 626
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    # ПІДЛЯГАЄ ПОВЕРНЕНЮ
    can.line(
        400, 691, 577, 691
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        401, 691, 401, 605
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        400, 605, 577, 605
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        576, 691, 576, 605
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    # судові данні
    can.line(
        400, 786, 526, 786
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        401, 785, 401, 706
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        400, 707, 525, 707
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        525, 785, 526, 706
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.setLineWidth(0)
    # місце штрих кода
    can.line(
        35, 800, 246, 800
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        35, 800, 35, 755
    )  # стіна (відстань від стіни, де починаєся, відстань від стіни, кінець лінії)
    can.line(
        246, 800, 246, 787
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    # де текст пишеся
    can.line(
        248, 773, 393, 773
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        248, 760, 393, 760
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        37, 740, 393, 740
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        37, 725, 393, 725
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        37, 710, 393, 710
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        37, 695, 393, 695
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # де текст пишеся 2
    can.line(
        510, 674, 573, 674
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        406, 660, 573, 660
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        406, 647, 573, 647
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        406, 635, 573, 635
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        406, 621, 573, 621
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # де текст пишеся судове
    can.line(
        403, 771, 523, 771
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        403, 756, 523, 756
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        403, 741, 523, 741
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        403, 724, 523, 724
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # лист
    can.line(
        53, 685, 53, 678
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        53, 685, 60, 685
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        60, 685, 60, 678
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        53, 678, 60, 678
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # бандероль
    can.line(
        123, 685, 123, 678
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        123, 685, 130, 685
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        130, 685, 130, 678
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        123, 678, 130, 678
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # посилка
    can.line(
        231, 685, 231, 678
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        231, 685, 238, 685
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        238, 685, 238, 678
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        231, 678, 238, 678
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # з оголошеною цінністю на грн
    can.line(
        179, 675, 179, 668
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        179, 675, 186, 675
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        186, 675, 186, 668
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        179, 668, 186, 668
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        309, 668, 349, 668
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # рекомендоване
    can.line(
        84, 668, 84, 661
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        84, 668, 91, 668
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        91, 668, 91, 661
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        84, 661, 91, 661
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # сума післяплати  грн  коп
    can.line(
        179, 661, 179, 654
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        179, 661, 186, 661
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        186, 661, 186, 654
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        179, 654, 186, 654
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        270, 654, 300, 654
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        318, 654, 336, 654
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # простий
    can.line(
        53, 638, 53, 631
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        53, 638, 60, 638
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        60, 638, 60, 631
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        53, 631, 60, 631
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # електронний
    can.line(
        123, 638, 123, 631
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        123, 638, 130, 638
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        130, 638, 130, 631
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        123, 631, 130, 631
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # Вищезазначене поштове відправлення, поштовий переказ
    can.line(
        35, 614, 35, 511
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        35, 614, 396, 614
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        396, 614, 396, 511
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        35, 511, 396, 511
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # вручено
    can.line(
        41, 588, 41, 595
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 588, 48, 588
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        48, 588, 48, 595
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 595, 48, 595
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # особисто
    can.line(
        41, 584, 41, 577
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 584, 48, 584
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        48, 584, 48, 577
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 577, 48, 577
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # за довіреністю
    can.line(
        41, 566, 41, 573
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 573, 48, 573
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        48, 566, 48, 573
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 566, 48, 566
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        120, 566, 216, 566
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # уповноваженому
    can.line(
        41, 553, 41, 560
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 560, 48, 560
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        48, 553, 48, 560
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        41, 553, 48, 553
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        120, 553, 216, 553
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        129, 540, 216, 540
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        216, 603, 216, 540
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    # виплачено та (дата)
    can.line(
        99, 595, 99, 588
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        99, 595, 106, 595
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        106, 595, 106, 588
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        99, 588, 106, 588
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        146, 588, 216, 588
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # не вручено
    can.line(
        219, 602, 219, 595
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 602, 226, 602
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        226, 602, 226, 595
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 595, 226, 595
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # не виплачено
    can.line(
        302, 602, 302, 595
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        302, 602, 309, 602
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        309, 602, 309, 595
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        302, 595, 309, 595
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # відмови адресата від одерження
    can.line(
        219, 582, 219, 575
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 582, 226, 582
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        226, 582, 226, 575
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 575, 226, 575
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # закінчення терміну зберігання
    can.line(
        219, 571, 219, 564
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 571, 226, 571
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        226, 571, 226, 564
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 564, 226, 564
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # неправильно зазначена або відсутня адреса
    can.line(
        219, 560, 219, 553
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 560, 226, 560
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        226, 560, 226, 553
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 553, 226, 553
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # інші причини
    can.line(
        219, 547, 219, 540
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 547, 226, 547
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        226, 547, 226, 540
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        219, 540, 226, 540
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        280, 539, 396, 539
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        43, 527, 396, 527
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        186, 516, 396, 516
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # повідомлення про вручення
    can.line(
        401, 588, 401, 511
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        401, 588, 575, 588
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        575, 588, 575, 511
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        401, 511, 575, 511
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    # відбитока календаря штемпелб
    can.line(
        529, 791, 529, 751
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        529, 791, 575, 791
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.line(
        575, 791, 575, 751
    )  # стіна (відстань від стіни, початок лінії, відстань від стіни, кінець лінії)
    can.line(
        529, 751, 575, 751
    )  # пряма лінія (де починаєся, висота, де закінчуєся, висота)
    can.save()
