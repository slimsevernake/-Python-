 $(document).ready(function ()
	  {  var h = 300, t = $('#tovar_desc'), max = t[0].scrollHeight, min = 0, scoreA = 0;
	   $('.read-next').on('click', function (event)
	  {
	   var H = t.height();
	   if(scoreA == 0){
	   	$('.read-next').addClass("read-next-arrow");
	   	scoreA = 1;
	   }else{
	   	$('.read-next').removeClass("read-next-arrow");
	   	scoreA = 0;
	   }

	   if(H == max){H = min}
	   else if (H  + h > max){H = max}
	   else {H += h};
	   t.height(H);
	   $(this).text(H == max ? 'Свернуть' : 'Читать далее')
	   return false
	  })
	  });
	 $(document).ready(function ()
	  {  var h = 10000, t = $('#comment_range'), max = t[0].scrollHeight, min = 522;
	   $('.read-next-fullcomment').on('click', function (event)
	  {
	   var H = t.height();
	   if(H == max){H = min}
	   else if (H  + h > max){H = max}
	   else {H += h};
	   t.height(H);
	   $(this).text(H == max ? 'Свернуть' : 'Читать все отзывы')
	   	if(H == max){
	   	$(this).addClass("read-next-arrow");
	   }else{
	   	$(this).removeClass("read-next-arrow");
	   }
	   return false
	  })
	  });
	 $(document).ready(function ()
	  {  var h = 10000, t = $('#user_comment'), max = t[0].scrollHeight, min = 52;
	   $('.read-next-comment').on('click', function (event)
	  {
	   var H = t.height();
	   if(H == max){H = min}
	   else if (H  + h > max){H = max}
	   else {H += h};
	   t.height(H);
	   $(this).text(H == max ? 'Свернуть' : 'Читать далее');
	   if(H == max){
	   	$(this).addClass("read-next-arrow");
	   }else{
	   	$(this).removeClass("read-next-arrow");
	   }
	   return false
	  })
	  });