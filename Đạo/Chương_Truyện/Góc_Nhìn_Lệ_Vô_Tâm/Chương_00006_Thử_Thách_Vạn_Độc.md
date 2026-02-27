<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>
<script src="../../../scripts/chapter_data.js"></script>
<script src="../../../scripts/navigation.js"></script>
<script src="../../../scripts/tts_player.js"></script>
<!-- NAVIGATION_END -->
# Chương 6: Thử Thách Vạn Độc
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
# Chương 6: Thử Thách Vạn Độc

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Quật - Bách Độc Trì.
**Thời điểm:** 3 ngày sau khi nhảy xuống Bách Độc Trì (Hữu Tâm 14 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Ba ngày ba đêm.

Ta trôi nổi trong Bách Độc Trì, lơ lửng giữa sự sống và cái chết. Da thịt ta bị ăn mòn, bong tróc từng mảng lớn, lộ ra cả xương trắng. Máu ta hòa vào chất độc, biến thành một màu tím đen kỳ dị.

Nhưng ta vẫn chưa chết.

Hơi thở của ta mỏng manh như tơ nhện, nhưng trái tim vẫn đập, từng nhịp, từng nhịp. [Tiểu Huyết](../../Kỳ_Vật/Tiểu_Huyết_Cổ.md) vẫn đang bám chặt vào lồng ngực ta, hút lấy chút sinh khí cuối cùng để nuôi dưỡng chính nó, và cũng để truyền lại cho ta một luồng độc khí bảo vệ tâm mạch.

Độc Cô Lão Quái đứng trên bờ, khoanh tay nhìn xuống. Ánh mắt lão không còn vẻ lạnh lùng như trước, mà thay vào đó là sự tò mò, thậm chí là một chút... hưng phấn.

"Kỳ tích," lão lẩm bẩm. "Mười bốn tuổi, chưa Trúc Cơ, mà chịu được ba ngày trong Bách Độc Trì. Thể chất của nó... quả thực sinh ra để dành cho độc đạo."

Lão phất tay. Một luồng kình phong nâng ta lên khỏi mặt hồ, đặt nằm xuống nền đá lạnh lẽo.

Ta mở mắt. Thế giới trước mắt ta mờ ảo, nhòe nhoẹt. Mọi thứ đều nhuốm một màu xanh lục ma quái. Ta cố gắng cử động ngón tay, nhưng cơ thể dường như không còn nghe lời ta nữa.

"Tỉnh rồi à?"

Giọng lão vang lên bên tai. "Cảm giác thế nào?"

Ta mấp máy môi, cổ họng khô khốc như sa mạc.

"Nóng..."

"Tốt. Nóng là tốt. Độc đang ngấm vào tủy xương. Nếu lạnh mới là chết."

Lão ngồi xuống cạnh ta, lấy ra một viên đan dược màu đỏ như máu chim bồ câu.

"Nuốt đi. [Huyết Sát Đan](../../Đan_Dược/Huyết_Sát_Đan.md). Nó sẽ giúp ngươi tái tạo da thịt, nhưng đồng thời cũng sẽ khiến độc tố trong người ngươi bùng phát dữ dội hơn gấp mười lần."

Lão nhét viên đan vào miệng ta, không đợi ta đồng ý.

Viên đan tan ngay trong miệng, biến thành một dòng dung nham chảy thẳng xuống dạ dày.

"Aaaaa!"

Ta cong người lên, gào thét thảm thiết. Cơn đau trước đó trong hồ độc chỉ như muỗi đốt so với cơn đau này. Từng thớ thịt, từng mạch máu như bị xé toạc ra, rồi lại được khâu lại bằng kim châm lửa.

Da ta bắt đầu mọc lại, nhưng không phải là làn da của con người nữa. Nó trơn bóng, dai như da rắn, và có màu xanh nhạt lấp lánh dưới ánh đuốc.

Tiểu Huyết trên ngực ta cũng biến đổi. Nó to lên gấp đôi, lớp vỏ cứng cáp hơn, đỏ rực như than hồng. Những cái chân tua tủa của nó cắm sâu vào da thịt ta, hòa làm một với cơ thể chủ nhân.

"Được rồi. Đã qua giai đoạn nguy hiểm nhất."

Độc Cô Lão Quái đứng dậy, gật gù hài lòng.

"Từ hôm nay, ngươi chính thức là đệ tử nhập thất của ta. Không còn là cái danh hão 'Thánh Tử' nữa. Ngươi sẽ được học *Vạn Độc Chân Kinh* bản gốc, chứ không phải cái thứ rác rưởi rút gọn mà đám ngoại môn đang tập."

Lão ném cho ta một cuốn sách cổ, bìa làm bằng da người, chữ viết bằng máu đen.

"Nhưng nhớ kỹ điều này: Con đường ngươi đi là độc đạo. Độc không có bạn bè. Độc không có người thân. Độc chỉ có một chủ nhân duy nhất."

Ta run rẩy cầm cuốn sách lên. Những ngón tay mới mọc da còn non nớt, nhưng ta cảm nhận được sức mạnh đang cuộn trào bên trong.

Ta quỳ xuống, dập đầu trước lão.

"Đệ tử... xin tạ ơn sư phụ."

Lão cười khẩy, quay lưng bỏ đi.

"Đừng vội cảm ơn. Thử thách thực sự mới chỉ bắt đầu thôi. Tháng sau là Huyết Nguyệt. Chuẩn bị tinh thần mà giữ lấy cái mạng chó của ngươi."

Ta nắm chặt cuốn sách, móng tay cắm sâu vào da thịt. Máu lại chảy ra, nhưng lần này ta không thấy đau nữa.

Ta thấy... mạnh mẽ.

*Vạn Độc Chân Kinh*. Ta sẽ luyện nó. Ta sẽ luyện đến mức cao nhất. Để không ai, không một ai có thể làm tổn thương ta được nữa.

Ta nhìn Tiểu Huyết, nó cũng đang nhìn ta. Đôi mắt bé xíu của nó ánh lên tia nhìn sắc lạnh.

"Chúng ta cùng nhau sống sót nhé, bạn hiền."
