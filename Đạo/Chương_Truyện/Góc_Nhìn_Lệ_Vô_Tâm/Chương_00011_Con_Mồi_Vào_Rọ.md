---
Tác_Giả: Jules (Tổng Quản)
Ngày_Viết: 2026-03-08
Góc_Nhìn: Lệ Vô Tâm
Bối_Cảnh: Ranh Giới Tử Thần - Rừng Huyết Độc
Nhân_Vật: Lệ Vô Tâm, Huyết Vệ
Ghi_Chú: Quan sát trận chiến giữa nhóm Diệp Tĩnh Sương và bầy Huyết Độc Lang.
---
<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00010_Mạng_Lưới_Tử_Thần.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px; color: #adb5bd;">Chương Sau ➡️</td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
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
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00011_Con_Mồi_Vào_Rọ.html">Chương 11: Con Mồi Vào Rọ</a></li>
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
# Chương 11: Con Mồi Vào Rọ

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Nhân vật liên quan:** [Diệp Tĩnh Sương](../../Nhân_Vật/Diệp_Tĩnh_Sương.md), [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md)
**Địa điểm:** [Rừng Huyết Độc](../../Thế_Giới_Và_Thời_Gian/Rừng_Huyết_Độc.md).
**Thời điểm:** Song song với [Chương 37](../Góc_Nhìn_Chính/Chương_00037_Vòng_Vây_Huyết_Lang.md) và [Chương 38](../Góc_Nhìn_Chính/Chương_00038_Huyết_Chiến_Lang_Vương.md).
**Giao Điểm Cốt Truyện:** Lệ Vô Tâm chứng kiến sức mạnh của Diệp Tĩnh Sương và quyết định dồn họ vào Vùng Đất Chết.

---

Tiếng sáo của ta réo rắt, len lỏi qua từng kẽ lá, hòa vào màn sương độc màu tím nhạt. Nó không phải là một bản nhạc để thưởng thức, mà là sợi dây cương vô hình, điều khiển hàng trăm con dã thú đang điên cuồng vì đói khát.

Ta đứng trên một cành *Huyết Mộc* cao vút, nhìn xuống "sân khấu" bên dưới.

Nhóm người của Diệp Tĩnh Sương đang vật lộn trong vòng vây. Ta phải thừa nhận, bọn họ kiên cường hơn ta tưởng. Tên nhãi con Lâm Phong bắn tên bách phát bách trúng, mỗi mũi tên đều găm đúng điểm yếu của lũ *Huyết Độc Lang*. Còn ả đàn bà Diệp Tĩnh Sương... chà, kiếm pháp của ả thật đẹp mắt.

Mỗi đường kiếm vung lên là một luồng hàn khí lạnh buốt tỏa ra, đóng băng cả không khí lẫn máu của lũ sói. *Hàn Ngọc Kiếm* trong tay ả như một con rồng bạc múa lượn, bảo vệ chặt chẽ cho hai mẹ con nhà họ Hứa.

"Khá lắm," ta lẩm bẩm, ngón tay lướt nhanh trên thân sáo. "Nhưng để xem các ngươi cầm cự được bao lâu."

Ta đổi nhịp điệu. Tiếng sáo trở nên dồn dập, sắc bén hơn.

Bên dưới, bầy sói lập tức thay đổi chiến thuật. Chúng không còn lao vào tấn công mù quáng nữa mà bắt đầu tản ra, bao vây và tấn công vào điểm yếu nhất: Hứa Nhược Thủy.

Ta thấy Diệp Tĩnh Sương nhíu mày. Ả nhận ra sự thay đổi này. Thông minh đấy. Nhưng nhận ra thì làm được gì? Ở đây, ta là chủ nhân, còn các ngươi chỉ là những con chuột trong lồng.

"Thánh Tử," Huyết Nhất thì thầm bên cạnh ta. "Có cần thuộc hạ xuống đó kết liễu bọn chúng không?"

"Không cần," ta phất tay. "Cứ để lũ sói chơi đùa thêm chút nữa. Ta muốn xem giới hạn của ả Thánh Nữ Kiếm Tông này đến đâu."

Nhưng sự kiên nhẫn của ta cũng có giới hạn. Khi thấy Lâm Phong dùng hỏa tiễn phá vỡ vòng vây, ta quyết định tung ra quân bài chủ lực.

Ta thổi một hơi dài, dồn linh lực vào tiếng sáo.

*GRÀOOOOO!*

*Huyết Độc Lang Vương* xuất trận.

Con quái vật khổng lồ với bộ giáp xương trắng hếu lao ra từ màn sương, mang theo áp lực của bậc Trúc Cơ. Ta mỉm cười đắc ý. Để xem các ngươi đối phó với nó thế nào.

Trận chiến diễn ra kịch liệt hơn ta dự tính. Diệp Tĩnh Sương không hề nao núng, ả chủ động tấn công Lang Vương, dùng *Hàn Băng Bộ* để né tránh và phản công. Còn tên nhãi Lâm Phong và thậm chí cả tên phế vật Hứa Thanh Vân cũng liều mạng xông lên.

Và rồi, khoảnh khắc ả đóng băng Lang Vương và tên nhãi kia bắn nát bụng nó... nụ cười trên môi ta tắt ngấm.

"Một lũ điên," ta rít lên qua kẽ răng. "Dám giết thú cưng của ta!"

Ta định lao xuống, đích thân bóp nát cổ từng đứa một. Nhưng hành động tiếp theo của chúng khiến ta khựng lại.

Thay vì chạy ngược trở lại sa mạc hay tìm đường vòng, chúng lại dìu nhau chạy thẳng vào cái hang động tối tăm, nơi tỏa ra thứ tử khí nồng nặc khiến ngay cả *Thiên Tinh Cổ* trong người ta cũng phải rùng mình.

"Vùng Đất Chết..." Huyết Nhất thốt lên, giọng lộ vẻ kinh hãi. "Thánh Tử, bọn chúng... bọn chúng tự sát sao?"

Ta đứng lặng nhìn theo bóng lưng bọn họ khuất dần trong bóng tối của cửa hang. Lũ sói còn lại gầm gừ bên ngoài, không dám bước tới nửa bước.

Bất chợt, ta bật cười. Tiếng cười vang vọng khắp khu rừng, hòa lẫn với tiếng gió rít.

"Thú vị! Thật thú vị!"

Ta thu sáo lại, ánh mắt lóe lên sự phấn khích tột độ.

"Chúng không tự sát đâu, Huyết Nhất. Chúng đang tìm đường sống trong chỗ chết. *Vùng Đất Chết*... nơi đó là cấm địa ngay cả với Tông Chủ. Nếu chúng chết trong đó, coi như xong. Còn nếu chúng sống sót trở ra..."

Ta bỏ lửng câu nói, quay người bước đi.

"Phong tỏa toàn bộ khu vực xung quanh cửa hang. Bất cứ thứ gì chui ra từ đó, dù là người hay quỷ, đều phải giết ngay lập tức."

"Tuân lệnh!"

Ta liếc nhìn về phía hang động một lần nữa. Diệp Tĩnh Sương, ta sẽ đợi. Đợi xem ngươi có thể làm nên kỳ tích gì trong cái huyệt mộ khổng lồ đó. Nếu ngươi chết, ngươi chỉ là kẻ tầm thường. Còn nếu ngươi sống...

...ngươi xứng đáng chết dưới tay ta.
