<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;"></div>
<script src="../../../scripts/chapter_data.js"></script>
<script src="../../../scripts/navigation.js"></script>
<script src="../../../scripts/tts_player.js"></script>
<!-- NAVIGATION_END -->
# Chương 5: Bóng Tối Cô Độc
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
