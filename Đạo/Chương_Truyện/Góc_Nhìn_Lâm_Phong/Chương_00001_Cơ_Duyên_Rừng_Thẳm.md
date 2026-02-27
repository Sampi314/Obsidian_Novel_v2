<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px; color: #adb5bd;">⬅️ Chương Trước</td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00002_Mũi_Tên_Đầu_Tiên.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_Cơ_Duyên_Rừng_Thẳm.html">Chương 1: Cơ Duyên Rừng Thẳm</a></li>
<li style="padding: 5px; "><a href="Chương_00002_Mũi_Tên_Đầu_Tiên.html">Chương 2: Mũi Tên Đầu Tiên</a></li>
<li style="padding: 5px; "><a href="Chương_00003_Rời_Khỏi_Rừng_Thẳm.html">Chương 3: Rời Khỏi Rừng Thẳm</a></li>
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
# Chương 1: Cơ Duyên Rừng Thẳm

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lâm Phong](../../Nhân_Vật/Lâm_Phong.md)
**Địa điểm:** Hắc Mộc Lâm (Nam Cương).
**Thời điểm:** 6 năm trước (Lâm Phong 12 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Mặt trời đứng bóng, chiếu những tia nắng gay gắt xuyên qua tán lá rậm rạp của Hắc Mộc Lâm. Nhưng dưới mặt đất, không khí vẫn ẩm ướt và mát lạnh, đặc trưng của khu rừng già ngàn năm tuổi này.

Ta, Lâm Phong, một đứa trẻ mười hai tuổi với làn da bánh mật và đôi mắt sáng như sao, đang nằm rạp trên một cành cây cổ thụ, tay nắm chặt cây cung gỗ sồi cũ kỹ của cha. Bên dưới, một con lợn rừng khổng lồ đang húc dũi vào gốc cây sồi già để tìm nấm mối.

"Bình tĩnh nào..." ta lầm bầm, cố gắng điều hòa nhịp thở.

Đây là lần đầu tiên cha cho phép ta đi săn một mình. Cả tuần nay, gia đình ta chỉ ăn cháo loãng với rau rừng. Mẹ đang ốm, cần thịt để tẩm bổ. Con lợn rừng này chính là hi vọng của cả nhà.

Ta kéo căng dây cung, mũi tên tre vót nhọn nhắm thẳng vào mắt con thú.

*Vút!*

Mũi tên xé gió lao đi. Nhưng đúng lúc đó, con lợn rừng đột ngột ngẩng đầu lên. Mũi tên cắm phập vào vai nó thay vì con mắt.

"Hộc!"

Con thú gầm lên đau đớn, lồng lộn quay đầu bỏ chạy vào sâu trong rừng.

"Chết tiệt!"

Ta vội vàng tụt xuống cây, lao theo vết máu loang lổ trên lá mục. Không thể để nó chạy thoát. Mũi tên của ta có tẩm nhựa cây độc, nó sẽ không chạy được xa đâu.

Ta đuổi theo con lợn rừng xuyên qua những bụi gai rậm rạp, băng qua những con suối cạn. Càng đi sâu vào rừng, không khí càng trở nên âm u và tĩnh lặng. Những cây cổ thụ ở đây to lớn dị thường, thân cây đen sì như than, cành lá vặn vẹo như những cánh tay ma quái.

Hắc Mộc Lâm. Khu vực cấm địa mà người già trong làng thường nhắc đến.

Ta rùng mình, nhưng nghĩ đến mẹ đang nằm liệt giường, ta cắn răng tiếp tục chạy.

Cuối cùng, ta tìm thấy con lợn rừng nằm gục trước cửa một hang động khuất sau dây leo chằng chịt. Nó đã chết.

Ta thở phào nhẹ nhõm, định bước tới kéo xác con thú về. Nhưng chân ta bỗng khựng lại.

Từ trong hang động tối om kia, một luồng sáng xanh nhạt le lói hắt ra, kèm theo đó là mùi hương thảo mộc thơm mát lạ kỳ. Nó không giống bất kỳ loài hoa nào ta từng ngửi thấy. Nó... thanh khiết, như gột rửa tâm hồn.

Sự tò mò của một đứa trẻ đã chiến thắng nỗi sợ hãi. Ta bỏ mặc con lợn rừng, rẽ đám dây leo bước vào hang.

Bên trong hang rộng hơn ta tưởng. Vách hang nhẵn thín, như thể được ai đó đẽo gọt. Ở giữa hang là một bệ đá phẳng lì, bên trên có một bộ hài cốt khô đét ngồi trong tư thế thiền định.

"Tiền bối..." Ta sợ hãi lùi lại, chắp tay vái lia lịa. "Con... con vô tình đi lạc, xin tiền bối tha tội..."

Nhưng bộ hài cốt vẫn im lìm. Trên tay nó đang nâng niu một chiếc hộp gỗ mộc mạc và một cuốn sách cũ kỹ.

Ta tiến lại gần hơn. Trên vách đá phía sau bộ hài cốt có khắc những dòng chữ cổ:

*"Ta là Thanh Mộc Tán Nhân, cả đời tu đạo cầu trường sinh, nhưng cuối cùng vẫn không thoát khỏi quy luật sinh tử. Nay thọ nguyên đã hết, ta để lại y bát tại đây. Kẻ nào hữu duyên tìm được, mong hãy dùng nó để hành thiện tích đức, đừng đi vào con đường tà đạo."*

Ta nuốt nước bọt, run run cầm lấy cuốn sách. Bìa sách làm bằng da thú, bên trên viết bốn chữ lớn: [Thanh Mộc Trường Sinh Quyết](../../Công_Pháp/Thanh_Mộc_Trường_Sinh_Quyết.md).

Khi ta lật trang đầu tiên, những dòng chữ bỗng nhiên phát sáng, bay lên không trung rồi chui tọt vào trán ta. Một luồng thông tin khổng lồ tràn ngập tâm trí, khiến đầu ta đau như búa bổ.

*Linh khí... Kinh mạch... Tu tiên...*

Ta ngã khuỵu xuống đất, ôm đầu rên rỉ. Nhưng cơn đau qua nhanh, thay vào đó là một cảm giác sảng khoái chưa từng có. Ta cảm nhận được luồng khí mát lạnh đang chạy dọc sống lưng, tụ lại ở bụng dưới.

Ta nhìn xuống tay mình. Những vết xước do gai rừng cào rách ban nãy đã biến mất không dấu vết.

"Đây là... phép thuật sao?"

Ta mở chiếc hộp gỗ ra. Bên trong là một cây cung ngắn màu xanh ngọc bích, dây cung trong suốt như tơ nhện nhưng dai chắc vô cùng. Bên cạnh là một ống tên chứa đầy những mũi tên làm từ gỗ Huyết Đằng đỏ thẫm.

[Truy Phong Cung](../../Luyện_Khí/Truy_Phong_Cung.md).

Ta cầm cây cung lên. Nó nhẹ bẫng trong tay ta, nhưng lại tỏa ra một sức mạnh tiềm tàng. Ta thử kéo dây cung. Không cần tốn quá nhiều sức, nhưng ta cảm giác như mình có thể bắn xuyên qua cả một tảng đá.

Ngày hôm đó, Lâm Phong, đứa trẻ thợ săn nghèo khó của Hắc Mộc Lâm đã chết. Thay vào đó là Lâm Phong, một tu sĩ Luyện Khí Kỳ, bước chân vào con đường tu tiên đầy chông gai nhưng cũng đầy kỳ diệu.

Ta quỳ xuống lạy bộ hài cốt ba lạy.

"Đa tạ sư phụ. Con hứa sẽ không phụ lòng người."

Ta đứng dậy, đeo Truy Phong Cung lên vai, giắt cuốn bí kíp vào ngực áo. Ta kéo xác con lợn rừng ra khỏi hang, lòng tràn đầy hi vọng. Mẹ sẽ khỏi bệnh. Và ta... ta sẽ khám phá thế giới rộng lớn ngoài kia, nơi mà những câu chuyện thần tiên không chỉ là truyền thuyết.
