<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00001_2_Bài_Học_Vô_Cảm.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_1_Hậu_Quả_Sinh_Tồn.html">Chương 1.1: Hậu Quả Sinh Tồn</a></li>
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
# Chương 1.1: Hậu Quả Sinh Tồn

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Môn (Hang động Tạp Dịch).
**Thời điểm:** Ngay sau sự kiện Huyết Trì (Hữu Tâm 13 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Đêm đầu tiên sau khi rời khỏi Huyết Trì, ta không thể ngủ.

Cơ thể ta rã rời, từng thớ thịt như muốn tách rời khỏi khung xương. Da thịt phồng rộp vì ngâm lâu trong độc huyết, cảm giác ngứa ngáy và đau rát xen lẫn khiến ta muốn điên lên. Nhưng cơn đau thể xác chẳng là gì so với cơn ác mộng đang chờ chực mỗi khi ta nhắm mắt.

*“Hữu Tâm ca ca...”*

Tiếng gọi của Tiểu Lan cứ văng vẳng bên tai ta, lúc gần lúc xa. Hình ảnh con rết khổng lồ cắn nát cổ họng nó, máu tươi bắn tung tóe... và rồi ánh mắt tuyệt vọng của nó khi chìm dần xuống đáy hồ. Ánh mắt ấy không oán trách, nhưng lại xoáy sâu vào tâm can ta như một lời nguyền rủa.

Ta bật dậy, mồ hôi lạnh toát ra như tắm.

Xung quanh ta là vách đá ẩm ướt của hang động dành cho đám tạp dịch mới nhập môn. Không chăn ấm nệm êm, chỉ có những bó rơm mục nát và mùi nấm mốc nồng nặc.

Ta nhìn xuống đôi bàn tay mình. Trong ánh trăng lờ mờ hắt vào từ cửa hang, ta vẫn thấy những vệt đỏ loang lổ. Dù ta đã kỳ cọ đến trầy da tróc vảy dưới suối, nhưng dường như màu máu của 98 đứa trẻ kia đã thấm sâu vào tận xương tủy.

"Quái vật..."

Ta nhớ lại ánh mắt của đám đệ tử ngoại môn khi nhìn thấy ta bước lên từ Huyết Trì. Kinh hãi, ghê tởm, và cả sự đề phòng. Không ai dám đến gần ta. Ngay cả những tên cai ngục vốn hung hăng cũng phải lùi lại vài bước.

Ta là kẻ sống sót duy nhất. Ta là "Thánh Tử" tương lai theo lời Độc Cô Lão Quái. Nhưng hiện tại, ta chỉ là một đứa trẻ cô độc giữa bầy sói.

Bụng ta réo lên cồn cào. Đã hai ngày ta chưa có gì bỏ vào bụng ngoài máu độc của con rết kia. Cơn đói cào xé ruột gan, nhưng cơn khát máu còn mãnh liệt hơn.

Ta lảo đảo đứng dậy, bước ra khỏi hang. Gió đêm ở Vạn Độc Môn lạnh buốt, mang theo mùi tử khí đặc trưng. Ta men theo con đường mòn dẫn xuống khu nhà bếp.

Ở đó, ta nhìn thấy một con chó hoang đang gặm xương thừa. Một con chó gầy trơ xương, lông rụng từng mảng lở loét. Nó nhìn thấy ta, gầm gừ đe dọa.

Bình thường, Hữu Tâm của ngày xưa sẽ sợ hãi bỏ chạy. Nhưng Hữu Tâm của bây giờ...

Ta cảm thấy một luồng nhiệt chạy dọc sống lưng. Đồng tử ta co lại. Ta không thấy con chó, ta chỉ thấy một khối thịt và máu đang di chuyển.

Ta lao tới.

Con chó sủa lên một tiếng kinh ngạc rồi chồm tới cắn ta. Nhưng ta nhanh hơn. Ta né được cú táp của nó, tay trái túm lấy gáy nó, đè nghiến xuống đất. Tay phải ta vớ lấy một hòn đá sắc cạnh bên đường.

*Bộp!*

Hòn đá đập mạnh vào đầu con chó. Nó rên ư ử, giãy giụa yếu ớt.

*Bộp! Bộp!*

Ta đập thêm hai nhát nữa. Máu văng lên mặt ta, nóng hổi. Mùi tanh nồng xộc vào mũi, nhưng thay vì buồn nôn, ta lại cảm thấy... hưng phấn. Cơn đói cồn cào trong bụng dịu đi một chút, thay vào đó là một cảm giác thỏa mãn kỳ lạ.

Ta buông tay. Con chó nằm bất động, óc trắng chảy ra hòa lẫn với máu.

Ta ngồi bệt xuống đất, thở hổn hển. Nhìn đôi tay nhuốm máu của mình, rồi nhìn xác con vật vô tội.

Nước mắt ta trào ra.

"Tiểu Lan... ta xin lỗi..." ta nấc lên, tiếng khóc nghẹn ngào trong cổ họng. "Ta không muốn... ta thực sự không muốn..."

Nhưng sâu thẳm trong ta, một giọng nói lạnh lẽo vang lên: *Khóc lóc cái gì? Muốn sống thì phải giết. Mày đã giết Tiểu Lan, giết cả đám bạn bè của mày. Bây giờ mày còn giả nhân giả nghĩa với một con chó sao?*

Ta lau nước mắt, nghiến chặt răng.

Đúng vậy. Hữu Tâm đã chết rồi. Chết ở dưới đáy Huyết Trì kia rồi.

Ta đứng dậy, đá cái xác con chó xuống vực thẳm.

Từ ngày mai, ta sẽ không khóc nữa. Ta sẽ sống. Sống để chứng minh cho thế giới này thấy, kẻ sống sót cuối cùng mới là kẻ mạnh nhất.
