<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>
<script src="../../../scripts/chapter_data.js"></script>
<script src="../../../scripts/navigation.js"></script>
<script src="../../../scripts/tts_player.js"></script>
<!-- NAVIGATION_END -->
# Chương 7: Huyết Nguyệt Sát Cơ
  <button onclick="speakChapter()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">▶️ Đọc</button>
  <button onclick="pauseSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏸️ Tạm Dừng</button>
  <button onclick="resumeSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏯️ Tiếp Tục</button>
  <button onclick="stopSpeech()" style="cursor: pointer; padding: 5px 10px; margin: 5px;">⏹️ Dừng</button>
</div>
<script>
var synth = window.speechSynthesis;
var utterance = null;

function speakChapter() {
  if (synth.speaking) {
    console.error("speechSynthesis.speaking");
    return;
  }
  // Clone body to Gỡ Bỏ navigation before reading
  var Nội Dung = document.body.cloneNode(true);
  var nav = Nội Dung.querySelector("#Chương-navigation");
  if (nav) {
    nav.Gỡ Bỏ();
  }
  var text = Nội Dung.innerText;
  utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "vi-VN";
  synth.speak(utterance);
}

function pauseSpeech() {
  if (synth.speaking && !synth.paused) {
    synth.pause();
  }
}

function resumeSpeech() {
  if (synth.paused) {
    synth.resume();
  }
}

function stopSpeech() {
  if (synth.speaking) {
    synth.cancel();
  }
}
</script>
</div>
<!-- NAVIGATION_END -->
# Chương 7: Huyết Nguyệt Sát Cơ

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn - Khu Rừng Cấm (Dành cho đệ tử nhập thất).
**Thời điểm:** Đêm Huyết Nguyệt (1 tháng sau - Hữu Tâm 14 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Đêm Huyết Nguyệt. Mặt trăng đỏ như máu treo lơ lửng giữa trời, soi rọi xuống Vạn Độc Môn một thứ ánh sáng ma quái.

Theo luật lệ của tông môn, vào đêm này, tất cả đệ tử nhập thất đều phải tham gia cuộc thi săn bắn trong Khu Rừng Cấm. Con mồi không phải là thú dữ, mà là chính những đồng môn của mình.

Mục tiêu rất đơn giản: Sống sót đến bình minh. Hoặc giết hết những kẻ khác.

Ta, Lệ Vô Tâm, đang núp trên cành cây cao nhất của một cây đại thụ cổ thụ. Cả người ta được phủ một lớp bùn trộn lẫn với *Hương Ẩn Thân* do ta tự chế, khiến ta hòa lẫn hoàn toàn vào vỏ cây xù xì.

Dưới gốc cây, ba bóng người đang thì thầm to nhỏ.

"Tìm kỹ đi! Con chuột nhắt đó chắc chắn ở quanh đây thôi!"

Đó là giọng của Lý Hổ, một tên đệ tử Luyện Khí tầng 8, nổi tiếng tàn bạo. Hắn đang dẫn theo hai tên đàn em đi săn ta.

"Đại ca, tên đó mới tầng 6, sao chúng ta phải huy động nhiều người thế?" Một tên đàn em làu bàu.

"Ngu xuẩn! Ngươi không nghe tin đồn sao? Nó sống sót qua Bách Độc Trì đấy! Huyết khí trên người nó là đại bổ cho việc luyện công. Nếu bắt được nó, rút xương lấy tủy, công lực của ta sẽ tăng vọt!"

Ta siết chặt con dao găm trong tay. Lưỡi dao được tẩm kịch độc chiết xuất từ *Tiểu Huyết*. Chỉ cần một vết xước nhỏ cũng đủ tiễn vong một tu sĩ Luyện Khí kỳ.

Bọn chúng đang tiến lại gần gốc cây ta đang ẩn nấp.

Ta nín thở. Tim đập thình thịch nhưng tâm trí lại lạnh băng. Đây là cơ hội tốt nhất để ta thử nghiệm *Vạn Độc Chân Kinh* tầng thứ nhất: *Độc Ảnh Bộ*.

Lý Hổ đứng ngay dưới chân ta, ngước nhìn lên tán cây rậm rạp.

"Lên kiểm tra xem!" Hắn ra lệnh.

Một tên đàn em bắt đầu leo lên. Hắn trèo thoăn thoắt như khỉ.

Khi đầu hắn vừa ló lên ngang tầm mắt ta, ta ra tay.

*Phập!*

Con dao găm cắm thẳng vào yết hầu hắn. Hắn trợn mắt, định hét lên nhưng máu đã chặn họng lại. Ta nhanh như chớp bịt miệng hắn, kéo mạnh vào trong tán lá.

*Rắc!*

Tiếng cổ gãy giòn tan. Ta ném xác hắn xuống đất.

"Cái gì?!" Lý Hổ giật mình lùi lại.

Cái xác rơi bộp xuống trước mặt hắn, mắt mở trừng trừng, máu đen chảy ra từ miệng.

"Nó ở trên đó! Giết nó!"

Lý Hổ gầm lên, vung đao chém loạn xạ vào thân cây. Tên đàn em còn lại cũng hoảng loạn phóng ám khí lên tán lá.

Nhưng ta không còn ở đó nữa.

Ta đã nhảy sang cành cây bên cạnh, nhẹ nhàng như một bóng ma. *Độc Ảnh Bộ* giúp ta di chuyển không tiếng động, thân pháp quỷ dị khó lường.

Ta đáp xuống sau lưng tên đàn em thứ hai.

"Ngươi tìm ai?" Ta thì thầm vào tai hắn.

Hắn giật bắn mình quay lại.

Ta thổi một luồng phấn độc màu tím vào mặt hắn.

"Á á á!"

Hắn ôm mặt gào thét, da thịt bắt đầu thối rữa, chảy nước vàng. Hắn lăn lộn dưới đất, cào cấu mặt mình trong cơn đau đớn tột cùng.

Lý Hổ kinh hoàng nhìn cảnh tượng trước mắt. Hai tên đàn em đắc lực của hắn bị hạ gục trong nháy mắt. Hắn nhìn quanh quất, mồ hôi vã ra như tắm.

"Ra đây! Đồ hèn nhát! Ra đây mà đấu tay đôi!"

Ta mỉm cười, bước ra từ bóng tối. Trên vai ta, Tiểu Huyết đang ngóc đầu dậy, đôi mắt đỏ rực nhìn hắn đầy thèm khát.

"Ta ở đây," ta nói, giọng bình thản. "Ngươi muốn lấy xương tủy ta sao? Đến mà lấy."

Lý Hổ thấy ta chỉ là một đứa trẻ gầy gò, Luyện Khí tầng 6, thì lấy lại chút bình tĩnh. Hắn gầm lên, vận toàn lực chém một đao về phía ta.

"Chết đi!"

Đao khí mang theo kình phong xé gió lao tới.

Ta không tránh. Ta giơ tay trái lên đỡ.

*Keng!*

Thanh đao chém vào cánh tay ta, nhưng không hề sứt mẻ da thịt. Chỉ để lại một vệt trắng mờ trên lớp vảy xanh nhạt.

"Cái... cái gì?!" Lý Hổ trợn mắt, không tin vào mắt mình. "Kim Cương Bất Hoại?! Không thể nào!"

"Không phải Kim Cương Bất Hoại," ta đáp, giọng lạnh lùng. "Là *Vạn Độc Thể*."

Ta tung chưởng phải vào ngực hắn. Bàn tay ta biến thành màu đen kịt, tỏa ra khói độc.

*Bốp!*

Lý Hổ bị đánh bay ra xa, đập vào gốc cây hộc máu tươi. Trên ngực hắn in hằn một dấu bàn tay đen sì đang lan rộng ra xung quanh.

"Ngươi... ngươi..." Hắn chỉ tay vào ta, run rẩy, rồi gục xuống chết ngay tức khắc. Độc tố đã phá nát tim phổi hắn.

Ta bước tới, nhìn ba cái xác nằm la liệt.

Ta không cảm thấy sợ hãi. Ta không cảm thấy tội lỗi. Ta chỉ cảm thấy... mạnh mẽ.

Ta ngồi xuống cạnh xác Lý Hổ, để Tiểu Huyết bò sang hút máu hắn.

Đêm Huyết Nguyệt vẫn còn dài. Và cuộc đi săn... mới chỉ bắt đầu.
