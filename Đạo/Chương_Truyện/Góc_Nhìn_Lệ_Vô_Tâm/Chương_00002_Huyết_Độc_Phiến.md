<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00002_2_Bẫy_Rập_Rừng_Sương.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00002_Huyết_Độc_Phiến.html">Chương 2: Huyết Độc Phiến</a></li>
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
# Chương 2: Huyết Độc Phiến

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Độc Trùng Cốc).
**Thời điểm:** 5 năm sau biến cố Huyết Trì (Lệ Vô Tâm 18 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Năm năm.
Đã năm năm kể từ ngày ta bò lên từ Huyết Trì.

Vạn Độc Môn không nuôi kẻ vô dụng. Danh hiệu "Thánh Tử" mà Độc Cô Lão Quái ban cho ta ngày đó, thực chất chỉ là một tấm bia ngắm bắn. Bất cứ tên đệ tử nào cũng muốn lấy đầu ta để chứng minh bản thân, để đoạt lấy sự ưu ái của Lão Quái.

Ta ngồi xếp bằng giữa Độc Trùng Cốc, xung quanh là sương mù độc chướng dày đặc đến mức tầm nhìn không quá ba bước chân. Trên người ta chằng chịt những vết sẹo, có cái đã lành, có cái vẫn còn rỉ máu xanh lè. [Vạn Độc Chân Kinh](../../Công_Pháp/Vạn_Độc_Chân_Kinh.md) tầng thứ ba đang vận hành điên cuồng trong kinh mạch, nuốt chửng từng luồng độc khí xung quanh.

"Vô Tâm sư đệ, trốn ở đây kỹ thế?"

Một giọng nói nhão nhoét vang lên, phá tan sự tĩnh lặng. Từ trong màn sương, một gã nam tử to béo bước ra. Hắn là Lý Tam, kẻ đứng đầu đám đệ tử ngoại môn, Luyện Khí tầng chín. Trên tay hắn cầm một thanh đại đao răng cưa, lưỡi đao đen sì tẩm kịch độc.

"Lý sư huynh," ta mở mắt, bình thản nhìn hắn. "Đến nộp mạng sao?"

Lý Tam cười lớn, tiếng cười rung chuyển cả lớp mỡ trên người hắn. "Khẩu khí lớn lắm. Nghe nói lão già kia mới ban cho ngươi một bộ xương cánh của Huyết Ưng Biến Dị. Giao nó ra đây, ta sẽ cho ngươi chết toàn thây."

Huyết Ưng Cốt. Đó là phần thưởng cho việc ta sống sót qua ba ngày trong Hầm Rắn Độc tháng trước. Một vật liệu thượng hạng để luyện khí.

"Muốn lấy?" Ta nhếch mép, từ từ đứng dậy. "Tự mình đến mà lấy."

Lý Tam gầm lên, vung đao chém xuống. Đao khí mang theo mùi hôi thối nồng nặc, xẻ toạc màn sương độc lao thẳng về phía ta.

Ta không tránh. Hay đúng hơn, ta không cần tránh.
Cơ thể ta khẽ rung lên, *Vạn Độc Phệ Hồn Quyết* kích hoạt. Một làn khói đen từ lỗ chân lông ta toát ra, ngưng tụ thành một lớp giáp mỏng manh nhưng kiên cố.

*Keng!*

Đại đao chém vào lớp khói đen, phát ra tiếng kim loại va chạm chói tai. Lý Tam trợn mắt kinh ngạc. Hắn không ngờ ta, một kẻ mới Luyện Khí tầng bảy, lại có thể đỡ đòn trực diện của hắn.

"Ngươi... ngươi đã luyện thành..."

"Độc Thể Sơ Thành," ta cắt lời hắn, giọng lạnh băng. "Cảm ơn sư huynh đã giúp ta kiểm chứng."

Không để hắn kịp phản ứng, ta lao tới. Tốc độ của ta nhanh như một con rắn hổ mang. Tay phải ta hóa thành trảo, móng tay đen dài sắc nhọn cắm phập vào cổ họng núc ních mỡ của hắn.

Máu phun ra, nhưng không rơi xuống đất. Ta vận công, hút lấy tinh huyết của hắn. Lý Tam giãy giụa yếu ớt, ánh mắt từ hung hãn chuyển sang van xin, rồi cuối cùng là tuyệt vọng.

Khi cái xác khô quắt của hắn đổ gục xuống đất, ta cảm thấy đan điền mình nóng rực. Linh lực của hắn, độc tố của hắn, tất cả đều trở thành dưỡng chất cho ta.

Ta lấy từ trong túi trữ vật ra bộ xương Huyết Ưng. Những đốt xương trắng toát, sắc lẹm, tỏa ra hàn khí âm u. Ta nhìn cái xác của Lý Tam, rồi nhìn bộ xương.

"Một bộ xương tốt, nhưng còn thiếu hồn."

Ta dùng móng tay rạch nát lồng ngực Lý Tam, rút ra một luồng oán khí đen ngòm đang lởn vởn quanh tim hắn. Đó là linh hồn đầy oán hận của kẻ vừa chết. Ta ép luồng oán khí đó vào trong bộ xương Huyết Ưng.

Lửa độc màu xanh lục bùng lên trong lòng bàn tay ta. Ta bắt đầu luyện chế.

Ba ngày ba đêm trôi qua.

Khi ngọn lửa tắt ngấm, trên tay ta không còn là bộ xương thô kệch nữa. Nó đã biến thành một chiếc quạt xếp tinh xảo. Nan quạt trắng bệch như xương người, mặt quạt mỏng như cánh ve dệt từ tơ độc, ẩn hiện những hình thù ma quái.

Ta khẽ phẩy nhẹ.
*Vù!*
Một cơn gió lốc màu xám tro quét qua, đám cỏ độc trước mặt lập tức khô héo, tan thành bụi phấn.

"Huyết Độc Phiến," ta thì thầm đặt tên cho nó.

Đây là vũ khí đầu tiên do chính tay ta tạo ra. Nó không chỉ là vũ khí, nó là minh chứng cho sự tồn tại của ta ở cái nơi cá lớn nuốt cá bé này.

Ta cài chiếc quạt vào thắt lưng, bước qua cái xác của Lý Tam. Giờ đây, ta đã có tư cách để bước vào Nội Môn, để tranh đoạt những thứ lớn hơn.

Độc Cô Lão Quái muốn nuôi một con Độc Vương. Được thôi, ta sẽ trở thành Độc Vương. Nhưng con Độc Vương này... sẽ có ngày quay lại cắn chết người nuôi nó.
