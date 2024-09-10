package com.example.test1.dao;

import java.util.HashMap;

import com.example.test1.model.Book;

public interface BookService {
	// 상품 불러오기
	HashMap<String, Object> getBookList(HashMap<String, Object> map);
	// 특정 상품 삭제하기
	HashMap<String, Object> selectBookDel(HashMap<String, Object> map);
	// 상품 가격 수정
	HashMap<String, Object> selectBookUpdate(HashMap<String, Object> map);
}
