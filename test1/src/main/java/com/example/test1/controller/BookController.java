package com.example.test1.controller;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.example.test1.dao.BookService;
import com.google.gson.Gson;

@Controller
public class BookController {
	
	@Autowired
	BookService bookService;
	
	// 책 리스트
	@RequestMapping("/book-list.do") 
    public String main(Model model) throws Exception {
        return "/book-list";
    }

	
	// 상품 불러오기
	@RequestMapping(value = "/book-list.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String getbookList(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = bookService.getBookList(map);
		return new Gson().toJson(resultMap);
	}
	
	// 특정 상품 삭제
	@RequestMapping(value = "/book-remove.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String removeBook(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = bookService.selectBookDel(map);
		return new Gson().toJson(resultMap);
	}
	
	// 가격 수정
	@RequestMapping(value = "/price-update.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String updatePrice(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = bookService.selectBookUpdate(map);
		return new Gson().toJson(resultMap);
	}
	

	

}


