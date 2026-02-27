<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>
<script src="../../../scripts/chapter_data.js"></script>
<script src="../../../scripts/navigation.js"></script>
<script src="../../../scripts/tts_player.js"></script>
<!-- NAVIGATION_END -->
# Chương 4: Sự Phản Bội Đầu Tiên
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
  // Clone body to remove navigation before reading
  var content = document.body.cloneNode(true);
  var nav = content.querySelector("#chapter-navigation");
  if (nav) {
    nav.remove();
  }
  var text = content.innerText;
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
# Chương 4: Sự Phản Bội Đầu Tiên

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Khu vực Dược Điền).
**Thời điểm:** 6 tháng sau (Hữu Tâm 14 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Sáu tháng ở Vạn Độc Môn dài như sáu thế kỷ. Ta đã học được cách ăn sâu bọ để sống, cách uống nước suối độc để tăng kháng tính, và cách giấu mình trong bóng tối để tránh những trận đòn vô cớ.

Nhưng điều ta vẫn chưa học được là cách để không cảm thấy cô đơn.

Cho đến khi ta gặp A Mộc.

A Mộc là một tên tạp dịch bị câm điếc làm việc ở Dược Điền phía tây núi. Hắn gầy gò, da đen nhẻm, luôn lầm lũi cúi đầu làm việc. Hắn không thể nói, cũng không thể nghe, nhưng ánh mắt của hắn lại ấm áp lạ thường.

Ngày đầu tiên ta trốn khỏi buổi huấn luyện khắc nghiệt, lạc vào Dược Điền, chính A Mộc đã giấu ta trong đống cỏ khô khi đám cai ngục đi tìm. Hắn chia cho ta nửa củ khoai lang nướng thơm lừng, còn mình thì gặm rễ cây.

Chúng ta trở thành bạn. Một tình bạn kỳ lạ giữa một "Thánh Tử" bị ghét bỏ và một tên tạp dịch thấp kém nhất.

Mỗi đêm, ta lén trốn ra Dược Điền gặp hắn. Ta kể cho hắn nghe về những cơn ác mộng, về nỗi sợ hãi của ta. Hắn lắng nghe chăm chú, đôi khi dùng những cử chỉ vụng về để an ủi ta. Ta dạy hắn vài chiêu thức phòng thân đơn giản mà ta học lỏm được. Hắn dạy ta cách phân biệt các loại thảo dược độc hại.

"A Mộc," ta viết lên nền đất bằng cành cây khô. "Một ngày nào đó, ta sẽ đưa huynh rời khỏi đây. Chúng ta sẽ đi thật xa, đến một nơi không có độc trùng, không có roi vọt."

Hắn nhìn dòng chữ, mỉm cười gật đầu lia lịa. Đôi mắt hắn sáng lên niềm hy vọng.

Ta tin hắn. Ta thực sự tin hắn. Vì hắn giống ta, đều là những kẻ bị thế giới này ruồng bỏ.

Nhưng ta đã sai.

Một đêm nọ, như thường lệ, ta lẻn đến Dược Điền.

"A Mộc!" Ta thì thào gọi.

Không có tiếng trả lời. Căn chòi lá của hắn trống trơn.

Bỗng nhiên, ánh đuốc sáng rực lên xung quanh.

"Bắt được rồi!"

Tiếng quát thô bạo vang lên. Hàng chục tên đệ tử Nội Môn xông ra từ bụi rậm, vây kín lấy ta. Dẫn đầu là Vương Thông, kẻ luôn ghen ghét với vị trí của ta.

Và đứng bên cạnh hắn... là A Mộc.

A Mộc không còn vẻ rụt rè sợ sệt nữa. Hắn đứng thẳng lưng, khuôn mặt lạnh tanh, trên tay cầm một túi tiền nặng trịch.

"A Mộc... huynh..." Ta lắp bắp, không tin vào mắt mình.

"Nó không câm đâu," Vương Thông cười khẩy, vỗ vai A Mộc. "Làm tốt lắm. Ngươi đã dụ được con chuột nhắt này ra khỏi hang ổ rồi."

A Mộc nhìn ta, ánh mắt không chút cảm xúc. Hắn mở miệng, giọng nói khàn khàn vang lên: "Xin lỗi, Thánh Tử. Nhưng mười viên linh thạch... quá lớn đối với một kẻ tạp dịch như ta."

Mười viên linh thạch.

Tình bạn của ta. Niềm tin của ta. Hy vọng của ta. Tất cả chỉ đáng giá mười viên đá vô tri ấy thôi sao?

"Tại sao?" Ta gào lên, giọng lạc đi vì đau đớn.

"Vì ở đây, không ai làm bạn với kẻ yếu," A Mộc đáp lại, lạnh lùng quay lưng bỏ đi. "Ngươi quá ngây thơ để sống sót ở Vạn Độc Môn này."

Vương Thông ra hiệu. Đám đệ tử lao vào đánh tới tấp. Ta không phản kháng. Ta nằm cuộn tròn dưới đất, chịu đựng những cú đá, cú đấm như mưa trút xuống người.

Đau. Đau lắm.

Nhưng nỗi đau thể xác này chẳng thấm vào đâu so với vết thương trong lòng ta đang rỉ máu.

Trái tim ta vỡ vụn.

Trong khoảnh khắc đó, Hữu Tâm – đứa trẻ luôn khao khát tình thương – đã chết hẳn.

Ta mở mắt. Đồng tử ta co lại thành một đường chỉ dọc như mắt rắn. Máu trong người ta sôi lên.

*Vạn Độc Phệ Hồn Quyết* tầng thứ nhất... tự động vận chuyển.

Một luồng khí đen kịt từ người ta bùng phát ra.

"Cút!"

Ta gầm lên. Một chưởng đánh ra, mang theo kình lực kinh người. Hai tên đệ tử đứng gần nhất bị đánh bay đi, hộc máu tươi.

Vương Thông kinh hãi lùi lại. "Cái quái gì thế này? Nó mới nhập môn sáu tháng mà!"

Ta đứng dậy, lảo đảo nhưng vững chãi. Máu chảy ròng ròng trên mặt, nhưng ta không lau. Ta nhìn chằm chằm vào bóng lưng A Mộc đang định rời đi.

"A Mộc!"

Hắn quay lại, vẻ mặt hoảng hốt.

Ta lao tới như một con thú hoang. Tốc độ nhanh đến mức Vương Thông cũng không kịp cản.

Năm ngón tay ta hóa thành trảo, cắm phập vào ngực trái của A Mộc.

*Phụt!*

Máu nóng hổi bắn lên mặt ta. Trái tim hắn... vẫn còn đập thoi thóp trong tay ta.

A Mộc trợn tròn mắt nhìn ta, miệng há hốc nhưng không nói được lời nào. Túi linh thạch rơi xuống đất, văng tung tóe.

"Bài học cuối cùng huynh dạy ta," ta thì thầm vào tai hắn, giọng lạnh băng như tiếng gọi của tử thần. "Cảm ơn."

Ta rút tay ra. A Mộc ngã gục xuống, chết không nhắm mắt.

Ta đứng giữa vòng vây, tay cầm trái tim đẫm máu, ngẩng đầu nhìn lên bầu trời đen kịt.

Không còn bạn bè. Không còn tin tưởng.
Chỉ có sức mạnh mới là vĩnh cửu.

Đêm đó, Lệ Vô Tâm thực sự ra đời.
