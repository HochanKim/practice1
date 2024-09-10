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
	.search {
		margin : 15px;
	}
	.upInput {
		margin-right:10px;
	}
	
	.updel {
		margin : 5px;
	}
	.info {
		padding-left:15px;
	}
</style>
<body>
	<div id="app">
		<input type="text" placeholder="제품번호를 입력하세요" v-model="productNo" class="search">
		<button @click="fnGetList('Y')">검색</button>
		<div v-if="info == 'Y'" class="info">
			<div>제품번호 : {{prod.productNo}}</div>
			<div>제품명 : {{prod.productName}}</div>
			<div>제품가격 : <span v-if="updateClick == 0">{{prod.productPrice}}</span> 
				<input type="text" placeholder="가격입력" v-model="productPrice" v-if="updateClick == 1" class="upInput">
				<button v-if="updateClick == 1" @click="fnSave">저장</button>
			</div>
			<button class="updel" @click="fnUpdate(1)">수정</button>
			<button class="updel" @click="fnRemove">삭제</button>
		</div>
	</div>
</body>
</html>
<script>
    const app = Vue.createApp({
        data() {
            return {
				prod : {},
				productNo : "",
				productName : "",
				productPrice : "",
				updateClick : 0,
				info : "N"
            };
        },
        methods: {
            fnGetList(info){
				var self = this;
				self.info = info; 
				var nparmap = {
					productNo : self.productNo
				};
				$.ajax({
					url:"test.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) { 
						console.log(data);
						self.prod = data.fruit;
					}
				});
            },
			fnRemove(){
				var self = this;
				var nparmap = {
					productNo : self.productNo
				};
				$.ajax({
					url:"remove.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) { 
						alert("삭제 됨");
						self.productNo = "";
						self.fnGetList('N');
					}
				});
			},
			fnUpdate(num){
				var self = this;
				self.updateClick = num;
			},
			fnSave(){
				var self = this;
				var nparmap = {
					productPrice : self.productPrice,
					productNo : self.productNo
				};
				$.ajax({
					url:"update.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) { 
						alert("수정 됨");
						self.updateClick = 0;
						self.productPrice = "";
						self.fnGetList('N');
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