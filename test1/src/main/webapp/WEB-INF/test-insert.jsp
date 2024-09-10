<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<jsp:include page="/layout/menu.jsp"></jsp:include>
	<title>테스트 샘플 파일</title>
</head>
<style>
	input {
		margin:10px 0;
	}
</style>
<body>
	<div id="app">
		<div>
			<div>
				제품명 : <input type=text v-model="productName">
			</div>
			<div>
				제품가격 : <input type=text v-model="productPrice"> 
			</div>
			<button @click="fnInsert">저장</button>
		</div>
	</div>
</body>
</html>
<script>
    const app = Vue.createApp({
        data() {
            return {
				productName : "",
				productPrice : "",
            };
        },
        methods: {
            fnInsert(){
				var self = this;
				var nparmap = {
					productName : self.productName,
					productPrice : self.productPrice
				};
				$.ajax({
					url:"insert.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) { 
						alert("저장 됨");
						location.href = 'test.do';
					}
				});
            }
        },
        mounted() {
			
        }
    });
    app.mount('#app');
</script>
​