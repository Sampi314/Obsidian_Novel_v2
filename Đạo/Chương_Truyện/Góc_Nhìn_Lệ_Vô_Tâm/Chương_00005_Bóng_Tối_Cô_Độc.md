<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_3_Sự_Phản_Bội_Đầu_Tiên.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00001_5_Thử_Thách_Vạn_Độc.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; "><a href="Chương_00001_1_Hậu_Quả_Sinh_Tồn.html">Chương 1.1: Hậu Quả Sinh Tồn</a></li>
<li style="padding: 5px; "><a href="Chương_00001_2_Bài_Học_Vô_Cảm.html">Chương 1.2: Bài Học Vô Cảm</a></li>
<li style="padding: 5px; "><a href="Chương_00001_3_Sự_Phản_Bội_Đầu_Tiên.html">Chương 1.3: Sự Phản Bội Đầu Tiên</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_4_Bóng_Tối_Cô_Độc.html">Chương 1.4: Bóng Tối Cô Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00001_5_Thử_Thách_Vạn_Độc.html">Chương 1.5: Thử Thách Vạn Độc</a></li>
<li style="padding: 5px; "><a href="Chương_00001_6_Huyết_Nguyệt_Sát_Cơ.html">Chương 1.6: Huyết Nguyệt Sát Cơ</a></li>
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
# Chương 1.4: Bóng Tối Cô Độc

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Hang động Tạp Dịch - Khu vực bị bỏ hoang).
**Thời điểm:** 1 tháng sau cái chết của A Mộc (Hữu Tâm 14 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

A Mộc đã chết. Hữu Tâm cũng đã chết.

Giờ đây, trong hang động lạnh lẽo này, chỉ còn lại một bóng ma lầm lũi tên là Lệ Vô Tâm.

Một tháng qua, ta không nói một lời nào. Ta tự cô lập mình trong một góc khuất của khu tạp dịch, nơi mà ngay cả lũ chuột cũng không buồn lui tới. Ta không còn trốn tránh đám đệ tử ngoại môn nữa, nhưng bọn chúng cũng không dám đến gần ta.

Ánh mắt của ta... Độc Cô Lão Quái nói đúng, ánh mắt của ta bây giờ giống hệt ánh mắt của một con rắn độc. Lạnh lẽo, vô cảm, và luôn chực chờ phun nọc độc.

Ta ngồi xếp bằng trên tảng đá, lòng bàn tay xòe ra. Một con rết nhỏ màu tím đang bò trườn trên da thịt ta.

"Mày đói rồi phải không?" Ta thì thầm, giọng khản đặc vì lâu ngày không nói.

Con rết ngẩng đầu lên, hai cái râu rung rinh như hiểu ý.

Ta lấy một con dao nhỏ, rạch nhẹ lên đầu ngón tay cái. Máu tươi rỉ ra, đỏ thẫm và có mùi hơi hăng hắc. Ta đưa ngón tay lại gần con rết. Nó lập tức bám lấy, tham lam hút lấy dòng máu nóng hổi.

Cảm giác đau nhói truyền đến, nhưng ta không hề nhăn mặt. Ta mỉm cười.

Đây là người bạn mới của ta. Nó không biết nói dối. Nó không biết phản bội. Nó chỉ cần máu của ta, và đổi lại, nó cho ta nọc độc.

Ta đặt tên cho nó là [Tiểu Huyết](../../Kỳ_Vật/Tiểu_Huyết_Cổ.md).

"Vô Tâm! Lão Quái gọi ngươi!"

Tiếng quát của một tên cai ngục vọng vào từ cửa hang. Hắn đứng tít ngoài xa, tay lăm lăm cây roi, nhưng không dám bước vào. Hắn sợ ta. Hay đúng hơn, hắn sợ cái xác chết khô quắt của A Mộc mà ta đã treo lủng lẳng trước cửa hang suốt ba ngày trước khi bị lôi đi.

Ta vuốt nhẹ Tiểu Huyết, để nó chui tọt vào trong ống tay áo rộng thùng thình.

"Ta biết rồi."

Ta đứng dậy, bước ra ánh sáng. Ánh nắng mặt trời chói chang khiến ta nheo mắt khó chịu. Ta đã quen với bóng tối. Bóng tối an toàn hơn. Trong bóng tối, ta là kẻ đi săn, không phải con mồi.

Trên đường đi đến Vạn Độc Quật, ta gặp Vương Thông. Hắn đang đi cùng đám tay chân, cười nói rôm rả.

Thấy ta, tiếng cười tắt ngấm. Vương Thông lùi lại một bước, tay vô thức đặt lên đốc kiếm. Ánh mắt hắn hiện lên vẻ kiêng kỵ rõ rệt.

Ta không nhìn hắn. Ta đi lướt qua hắn như thể hắn chỉ là một tảng đá ven đường.

"Thằng nhãi ranh..." Hắn lầm bầm chửi rủa sau lưng ta, nhưng không dám ra tay.

Ta nhếch mép. Sợ hãi. Đó là thứ vũ khí tuyệt vời nhất. Khi người ta sợ ngươi, người ta sẽ không dám làm tổn thương ngươi. Ít nhất là trước mặt.

Ta bước vào Vạn Độc Quật. Độc Cô Lão Quái đang đợi ta bên cạnh một cái hồ nhỏ chứa đầy chất lỏng màu xanh lục sủi bọt.

"Đến rồi à?" Lão không quay lại, giọng nói vẫn đều đều vô cảm. "Tháng vừa rồi ngươi làm khá lắm. Tự mình luyện được *Huyết Dẫn Cổ* sơ cấp."

Lão biết. Tất nhiên là lão biết. Không gì qua mắt được lão già quái vật này.

"Con rết đó đâu?"

Ta lấy Tiểu Huyết ra, đặt lên bàn tay lão. Con rết co rúm lại, sợ hãi trước khí tức kinh khủng tỏa ra từ người lão.

"Tốt. Rất có tiềm năng." Lão gật đầu, ném con rết trả lại cho ta. "Nhưng còn quá yếu. Muốn nó trở thành [Bản Mệnh Cổ](../../Kỳ_Vật/Bản_Mệnh_Cổ.md), ngươi cần nhiều hơn là máu của chính mình."

Lão chỉ tay xuống cái hồ xanh lục.

"Nhảy xuống đi."

Ta nhìn cái hồ. *Vạn Độc Trì*. Nơi chứa nọc độc của hàng ngàn loài rắn rết, bọ cạp. Nhảy xuống đó, cửu tử nhất sinh.

Nhưng ta không do dự.

Ta cởi áo ngoài, để lộ cơ thể gầy gò chằng chịt sẹo. Ta ôm Tiểu Huyết vào lòng, rồi nhảy ùm xuống.

Chất độc ngấm vào da thịt, đau đớn như bị lột da sống. Ta cắn chặt răng, không hét lên một tiếng.

Trong cơn đau đớn tột cùng, ta lại thấy A Mộc. Hắn đang cười với ta, nụ cười giả tạo ghê tởm.

*Ta sẽ sống. Ta sẽ mạnh hơn. Ta sẽ khiến tất cả các người phải quỳ dưới chân ta.*

Ta nhắm mắt, để mặc cho bóng tối nuốt chửng lấy mình. Trong bóng tối đó, ta không còn cô đơn nữa. Ta có độc dược. Ta có hận thù.

Và thế là đủ.
