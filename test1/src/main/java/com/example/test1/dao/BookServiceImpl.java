package com.example.test1.dao;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.test1.mapper.BookMapper;
import com.example.test1.model.Book;


@Service
public class BookServiceImpl implements BookService{

	@Autowired
	BookMapper bookMapper;


	@Override
	public HashMap<String, Object> getBookList(HashMap<String, Object> map) {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		List<Book> list = bookMapper.getBookList(map);
		resultMap.put("list", list);
		return resultMap;
	}


	@Override
	public HashMap<String, Object> selectBookDel(HashMap<String, Object> map) {
		HashMap<String, Object> removeMap = new HashMap<String, Object>();
		bookMapper.selectBookDel(map);
		System.out.println("삭제된 책 : "+map);
		return removeMap;
	}


	@Override
	public HashMap<String, Object> selectBookUpdate(HashMap<String, Object> map) {
		HashMap<String, Object> updateMap = new HashMap<String, Object>();
		bookMapper.selectBookUpdate(map);
		System.out.println("수정 가격 : "+map);
		return updateMap;
	}


}
