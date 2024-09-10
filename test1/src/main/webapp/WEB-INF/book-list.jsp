<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<jsp:include page="/layout/menu.jsp"></jsp:include>
	<title>첫번째 페이지</title>
</head>
<style>
	table {
		margin:20px;
	}
    table,
    tr,
    td,
    th {
        border: 1px solid;
        text-align: center;
        border-collapse: collapse;
    }

    tr,
    td,
    th {
		height:40px;
        padding: 5px 10px;
    }
	.title {
		width:300px;
	}
	.cdate {
		width:200px;
	}
	a {
		color:#000;
		font-weight:bold;
	}
	.category > li {
		display:inline-block;
		width:100px;
		text-align:center;
		margin:10px;
		
		border:1px solid black;
	}

	button {
		margin:0 20px;
	}
</style>
<body>
	<div id="app">
		<table>
			<tr>
				<th>번호</th>
				<th>제목</th>
				<th>출판사</th>
				<th>가격</th>
				<th>삭제</th>
				<th>수정</th>
			</tr>
			<tr v-for="item in bookList">
				<td>{{item.bookId}}</td>
				<td>{{item.bookName}}</td>
				<td>{{item.publisher}}</td>
				<td>
					<template v-if="!isPriceUpdate">
						{{item.price}}
					</template>
					<template v-else>
						<input type="text" v-model="item.price">
					</template>
				</td>
				<td>
					<button @click="selectRemove(item.bookId)">삭제</button>
				</td>
				<td>
					<template v-if="!isPriceUpdate">
						<button @click="selectUpdate(item.bookId)">수정</button>
					</template>
					<template v-else>
						<button @click="updateSend(item.price)">수정</button>
					</template>
				</td>
			</tr>
		</table>
	</div>
</body>
</html>
<script>
    const app = Vue.createApp({
        data() {
            return {
               	bookList : [],
				bookId : "",
				price : "",
				isPriceUpdate : false,
            };
        },
        methods: {
            fnGetList(){	// 'book' 테이블 데이터 불러오기 (list 형태)
				var self = this;
				var nparmap = {};
				$.ajax({
					url:"book-list.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) {
						console.log(data);
						self.bookList = data.list;
					}
				});
            },

			selectRemove(number){		// 삭제 버튼
				var self = this;
				if(!confirm("삭제하시겠습니까?")){
					return;
				}
				var nparmap = {
					bookId : number
				};
				$.ajax({
					url:"book-remove.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) {
						alert("삭제되었음!");
						self.fnGetList();
					}
				});
            },

			selectUpdate(number){	// 수정 버튼 (가격)
				var self = this;
				self.bookId = number;
				console.log("클릭 아이디 : "+number);
				self.isPriceUpdate = true;
			},

			updateSend(newPrice){	// 수정 가격 보내기
				var self = this;
				var nparmap = {
					bookId : self.bookId,
					price : newPrice
				};
				$.ajax({
					url:"price-update.dox",
					dataType:"json",	
					type : "POST", 
					data : nparmap,
					success : function(data) {
						alert("수정됨!");
						self.isPriceUpdate = false;
						self.fnGetList();
					}
				});
			}
        },
        mounted() {
            var self = this;
			self.fnGetList();
        }
    });
    app.mount('#app');
</script>