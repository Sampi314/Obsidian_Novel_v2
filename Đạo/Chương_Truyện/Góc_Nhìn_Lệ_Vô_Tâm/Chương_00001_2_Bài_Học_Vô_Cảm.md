<!-- NAVIGATION_START -->
<div id="chapter-navigation" style="text-align: center; margin-bottom: 20px;">
<table style="width: 100%; text-align: center; border: none;">
<tr>
<td style="border: none; padding: 5px;"><a href="Chương_00001_1_Hậu_Quả_Sinh_Tồn.html">⬅️ Chương Trước</a></td>
<td style="border: none; padding: 5px;"><a href="../../../index.html">🏠 Trang Chủ</a></td>
<td style="border: none; padding: 5px;"><a href="index.html">📖 Mục Lục</a></td>
<td style="border: none; padding: 5px;"><a href="Chương_00001_3_Sự_Phản_Bội_Đầu_Tiên.html">Chương Sau ➡️</a></td>
</tr>
</table>
<details style="margin-top: 10px;">
<summary style="cursor: pointer; font-weight: bold;">Chọn Chương</summary>
<ul style="max-height: 200px; overflow-y: auto; list-style: none; padding: 0; text-align: left;">
<li style="padding: 5px; "><a href="Chương_00001_Đường_Đến_Thánh_Vị.html">Chương 1: Đường Đến Thánh Vị</a></li>
<li style="padding: 5px; "><a href="Chương_00001_1_Hậu_Quả_Sinh_Tồn.html">Chương 1.1: Hậu Quả Sinh Tồn</a></li>
<li style="padding: 5px; font-weight: bold; background-color: #f0f0f0;"><a href="Chương_00001_2_Bài_Học_Vô_Cảm.html">Chương 1.2: Bài Học Vô Cảm</a></li>
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
# Chương 1.2: Bài Học Vô Cảm

**Tác giả:** Tổng Quản (Jules)
**Góc nhìn:** [Lệ Vô Tâm](../../Nhân_Vật/Lệ_Vô_Tâm.md)
**Địa điểm:** Vạn Độc Quật.
**Thời điểm:** 3 ngày sau sự kiện Huyết Trì (Hữu Tâm 13 tuổi).
**Giao Điểm Cốt Truyện:** Tuyến độc lập (Quá khứ).

---

Vạn Độc Quật sâu thẳm dưới lòng đất, nơi mà ánh sáng mặt trời vĩnh viễn không chạm tới. Ở đây chỉ có tiếng róc rách của những dòng suối ngầm chứa độc dược, tiếng kêu rít của hàng vạn loài côn trùng lạ lùng, và tiếng roi vút trong không khí.

*Chát!*

Một ngọn roi da rắn quất mạnh vào lưng ta, xé toạc lớp áo vải thô, để lại một vết hằn tím bầm rỉ máu.

"Đau không?"

Giọng nói khàn đục của Độc Cô Lão Quái vang lên, lạnh lùng và vô cảm. Lão ngồi trên tảng đá lớn, tay cầm chén trà bốc khói, ánh mắt hờ hững nhìn ta đang quỳ gối dưới đất.

"Đ... đau..." Ta lí nhí, cắn chặt môi để không bật ra tiếng rên rỉ.

*Chát!*

Nhát roi thứ hai quất xuống, chồng lên vết thương cũ.

"Trả lời lại!" Lão quát.

"Đau!" Ta gào lên, nước mắt ứa ra vì đau đớn tột cùng.

*Chát! Chát! Chát!*

Ba nhát roi liên tiếp quất xuống như mưa. Ta ngã sấp xuống, toàn thân co rúm lại. Máu tươi thấm đẫm lưng áo, chảy ròng ròng xuống nền đá lạnh lẽo.

"Đứng dậy!"

Ta lồm cồm bò dậy, hai chân run rẩy. Ta ngước nhìn lão, ánh mắt vừa sợ hãi vừa căm phẫn. Tại sao lão lại đánh ta? Ta đã làm gì sai? Ta là Thánh Tử cơ mà?

Độc Cô Lão Quái bước xuống, dùng mũi giày nâng cằm ta lên, buộc ta phải nhìn thẳng vào mắt lão.

"Ngươi biết tại sao ta đánh ngươi không?"

Ta lắc đầu.

"Vì ngươi đau. Vì ngươi khóc. Vì ngươi yếu đuối."

Lão buông cằm ta ra, quay lưng đi về phía một cái lồng sắt lớn ở góc hang. Trong lồng là một con khỉ nhỏ đang run rẩy co cụm.

"Cầm lấy."

Lão ném cho ta một con dao găm sắc lẹm.

"Giết nó."

Ta sững người. Giết con khỉ? Nó trông thật tội nghiệp, đôi mắt to tròn ngập nước giống hệt... giống hệt Tiểu Lan.

"Sư... sư phụ... con không..."

"Giết nó, hoặc ta sẽ chặt đứt một ngón tay của ngươi."

Ta nhìn con dao, rồi nhìn con khỉ. Lại nhìn bàn tay của mình. Mười ngón tay vẫn còn nguyên vẹn, nhưng ta biết lão già này nói được làm được.

Ta run rẩy bước tới cái lồng. Con khỉ thấy ta cầm dao, càng co rúm lại, kêu *chí chóe* van xin.

Ta không thể. Ta không thể giết nó. Nó không làm gì ta cả.

"Ta đếm đến ba," giọng lão vang lên sau lưng, lạnh như băng. "Một."

Tay ta run bần bật. Con dao chực rơi xuống đất.

"Hai."

Ta nhắm mắt lại. Hình ảnh Tiểu Lan hiện lên trong tâm trí. *Hữu Tâm ca ca, muội sợ lắm...*

"Ba."

*Vút!*

Một luồng kình phong lướt qua tai ta.

*Phập!*

Ngón út bàn tay trái của ta bay vèo xuống đất, máu phun ra như suối.

"Aaaaa!"

Ta hét lên đau đớn, ôm lấy bàn tay cụt ngón, ngã quỵ xuống.

Độc Cô Lão Quái đứng sừng sững trước mặt ta, trên tay cầm thanh kiếm dính máu của ta.

"Ta đã nói rồi. Lòng trắc ẩn là thứ độc dược chết người nhất. Hôm nay là ngón út. Ngày mai, nếu ngươi còn do dự, sẽ là cái đầu của ngươi."

Lão đá văng cái lồng sắt, con khỉ sợ hãi chạy biến vào bóng tối.

"Tự băng bó đi. Rồi quay lại đây ngâm mình trong [Bách Độc Trì](../../Kỳ_Vật/Bách_Độc_Trì.md) hai canh giờ. Nếu ngất xỉu, ta sẽ ném xác ngươi cho lũ rết ăn."

Lão bỏ đi, để lại ta một mình trong hang động tối tăm, với bàn tay đầm đìa máu và nỗi đau thấu tim gan.

Ta nhìn ngón tay bị cắt lìa nằm lăn lóc trên đất. Nó tím tái, co quắp.

Bài học đầu tiên: Ở Vạn Độc Môn, không có chỗ cho nước mắt. Không có chỗ cho sự do dự.

Ta xé vạt áo, băng chặt vết thương. Cơn đau làm ta tỉnh táo lạ thường.

Ta thề, đây sẽ là lần cuối cùng ta khóc vì đau. Lần cuối cùng ta mất đi một phần cơ thể vì sự yếu đuối của chính mình.

Ta bước xuống Bách Độc Trì, dòng nước đen ngòm sủi bọt.

Nóng. Rát. Như ngàn kim châm.

Nhưng ta không hét lên. Ta cắn chặt răng, nuốt ngược tiếng rên vào trong bụng.

*Vô Tâm. Phải vô tâm mới sống được.*
