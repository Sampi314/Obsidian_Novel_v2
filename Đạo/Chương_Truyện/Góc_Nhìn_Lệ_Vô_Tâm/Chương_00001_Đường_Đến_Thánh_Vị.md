<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px; color: #adb5bd;">⬅️ Chương Trước</td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00001_1_Hậu_Quả_Sinh_Tồn.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; "><a href="Chương_00001_1_Hậu_Quả_Sinh_Tồn.html">Chương 1.1: Hậu Quả Sinh Tồn</a></li>
<li style="padding: 5px; "><a href="Chương_00001_2_Bài_Học_Vô_Cảm.html">Chương 1.2: Bài Học Vô Cảm</a></li>
<li style="padding: 5px; "><a href="Chương_00001_3_Sự_Phản_Bội_Đầu_Tiên.html">Chương 1.3: Sự Phản Bội Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Huyết_Độc_Phiến.html">Chương 2: Huyết Độc Phiến</a></li>
<li style="padding: 5px; "><a href="Chương_00002_2_Bẫy_Rập_Rừng_Sương.html">Chương 2.2: Bẫy Rập Rừng Sương</a></li>
<li style="padding: 5px; "><a href="Chương_00002_5_Diệt_Môn_Chi_Họa.html">Chương 2.5: Diệt Môn Chi Họa</a></li>
<li style="padding: 5px; "><a href="Chương_00002_8_Thanh_Trừng_Nội_Bộ.html">Chương 2.8: Thanh Trừng Nội Bộ</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Mệnh_Lệnh_Bóng_Tối.html">Chương 3: Mệnh Lệnh Bóng Tối</a></li>
<li style="padding: 5px; "><a href="Chương_00004_Thí_Nghiệm_Máu.html">Chương 4: Thí Nghiệm Máu</a></li>
<li style="padding: 5px; "><a href="Chương_00005_Ván_Cờ_Huyết_Độc.html">Chương 5: Ván Cờ Huyết Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00006_Truy_Vết_Tử_Thần.html">Chương 6: Truy Vết Tử Thần</a></li>
<li style="padding: 5px; "><a href="Chương_00007_Dưới_Bóng_Hắc_Sa.html">Chương 7: Dưới Bóng Hắc Sa</a></li>
<li style="padding: 5px; "><a href="Chương_00008_Huyết_Tế_Sa_Mạc.html">Chương 8: Huyết Tế Sa Mạc</a></li>
<li style="padding: 5px; "><a href="Chương_00009_Sát_Ý_Rừng_Gai.html">Chương 9: Sát Ý Rừng Gai</a></li>
<li style="padding: 5px; "><a href="Chương_00010_Mạng_Lưới_Tử_Thần.html">Chương 10: Mạng Lưới Tử Thần</a></li>
<li style="padding: 5px; "><a href="Chương_00011_Con_Mồi_Vào_Rọ.html">Chương 11: Con Mồi Vào Rọ</a></li>
</ul>
</details>
<div style="margin-top: 15px; border-top: 1px solid #ccc; padding-top: 10px;">
  <strong>🎧 Nghe Chương Này:</strong>
  <br>
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
# Chương 1: Đường Đến Thánh Vị

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Huyết Trì).
**Thời điểm:** 10 năm trước (Hữu Tâm 13 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Máu. Mùi tanh nồng của máu lấp đầy khoang mũi ta, đặc quánh đến mức ta cảm tưởng như mình đang hít thở trong một bể nước đỏ lòm. Mà thực tế thì đúng là như vậy.

Ta, Hữu Tâm — cái tên mà cha mẹ đã đặt cho ta với mong ước ta sống một đời có tình có nghĩa — khi ấy chỉ là một đứa trẻ mười ba tuổi gầy gò, đang ngâm mình trong Huyết Trì cùng với chín mươi chín đứa trẻ khác. Chúng ta đều là những cô nhi, những kẻ bị cha mẹ bỏ rơi, bị bán đi, hoặc bị bắt cóc từ những ngôi làng biên giới. Chúng ta được đưa về đây, Vạn Độc Môn, không phải để được nuôi dưỡng, mà để trở thành *thức ăn*.

"Kẻ sống sót cuối cùng sẽ là Thánh Tử."

Giọng nói khàn đục của Độc Cô Lão Quái vang lên từ trên bờ đá cao ngất, lạnh lùng và vô cảm như tiếng gọi của tử thần.

Ta nhìn sang bên cạnh. Một đứa bé gái trạc tuổi ta, đôi mắt to tròn ngập nước, tay nắm chặt vạt áo rách rưới. Nó tên là Tiểu Lan. Mới hôm qua thôi, nó còn chia cho ta nửa cái bánh bao mốc meo mà nó giấu được.

*“Hữu Tâm ca ca, muội sợ lắm...”*

Tiếng thì thầm của nó vừa dứt thì một con rết khổng lồ từ đáy hồ trồi lên, hàm răng sắc nhọn cắm phập vào cổ nó. Máu phun ra, hòa vào dòng nước vốn đã đỏ ngầu. Tiểu Lan không kịp hét lên tiếng nào, thân xác nhỏ bé lập tức bị kéo tuột xuống đáy sâu.

Ta không hét lên. Ta cũng không khóc. Trong khoảnh khắc đó, Hữu Tâm đã chết đi, và một thứ khác... đen tối hơn, lạnh lẽo hơn... bắt đầu trỗi dậy.

Sợ hãi? Vô ích.
Cầu xin? Nực cười.
Ở cái nơi địa ngục này, lòng trắc ẩn là thứ độc dược chết người nhất. Muốn sống, ta phải trở thành kẻ ác nhất.

Ta lặn xuống, không phải để trốn chạy, mà để tìm kiếm. Ta tìm thấy xác của Tiểu Lan, và cả con rết đang ngấu nghiến nó. Ta rút ra mảnh xương sườn sắc nhọn mà ta đã lén mài từ xác của một đứa trẻ khác đã chết hôm trước.

*Phập!*

Ta đâm mạnh vào mắt con rết. Nó quằn quại, điên cuồng quẫy đạp. Ta bám chặt lấy lưng nó, mặc cho lớp vỏ cứng cứa vào da thịt ta ứa máu. Ta cắn. Đúng, ta cắn vào vết thương của nó, uống lấy dòng máu độc màu xanh lục đang chảy ra.

Cơn đau đớn như thiêu đốt lục phủ ngũ tạng ập đến. Ta cảm thấy như có ngàn vạn con kiến lửa đang gặm nhấm từng thớ thịt. Nhưng ta không buông tay. Ta uống, uống đến khi bụng căng cứng, uống đến khi con rết kia lịm đi vì mất máu.

Khi ta trồi lên mặt nước lần nữa, chín mươi tám đứa trẻ còn lại đều nhìn ta bằng ánh mắt kinh hoàng. Chúng thấy một con quỷ dữ, toàn thân nhuộm máu xanh đỏ lẫn lộn, đôi mắt rực lên ánh sáng man dại.

"Giết," ta gầm lên, giọng nói không còn là của một đứa trẻ.

Đêm đó, Huyết Trì dậy sóng. Ta không nhớ mình đã giết bao nhiêu người, hay bao nhiêu con độc trùng. Ta chỉ nhớ cảm giác máu nóng hổi chảy qua kẽ tay, nhớ tiếng xương gãy giòn tan dưới chân mình.

Khi bình minh lên, chỉ còn một mình ta đứng vững giữa biển xác chết.

Độc Cô Lão Quái bước xuống, nhìn ta với ánh mắt hài lòng hiếm thấy. Lão đưa bàn tay khô khốc vuốt lên trán ta, để lại một dấu ấn đau rát.

"Từ nay, cái tên Hữu Tâm đã chết. Ngươi là Vô Tâm. Lệ Vô Tâm."

Ta quỳ xuống, cúi đầu thật thấp, che giấu nụ cười méo mó trên môi.

*Tiểu Lan à, cái bánh bao đó... ta đã trả lại bằng chín mươi tám mạng người và cả một con Huyết Rết ngàn năm. Đủ chưa?*
