package com.example.test1.mapper;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.example.test1.model.Book;


@Mapper
public interface BookMapper {
	// 상품 가져오기
	List<Book> getBookList(HashMap<String, Object> map);
	// 특정 상품 삭제하기
	void selectBookDel(HashMap<String, Object> map);
	// 상품 가격 수정
	void selectBookUpdate(HashMap<String, Object> map);
}
