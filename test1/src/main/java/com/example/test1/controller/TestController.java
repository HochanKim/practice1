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

import com.example.test1.dao.TestService;
import com.example.test1.model.Test;
import com.google.gson.Gson;

@Controller
public class TestController {
	
	@Autowired
	TestService testService;
	
	@RequestMapping("/test.do") 
    public String main(Model model) throws Exception {
        return "/test-list";
    }
	
	@RequestMapping("/insert.do") 
	public String insert(Model model) throws Exception {
		return "/test-insert";
	}
	
	@RequestMapping("/lists.do") 
	public String search(Model model) throws Exception {
		return "/test-table";
	}
	
	// 상품 불러오기
	@RequestMapping(value = "/test.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String searchBbsList(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = testService.getProductInfo(map);
		return new Gson().toJson(resultMap);
	}
	
	// 상품 삭제
	@RequestMapping(value = "/remove.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String removeList(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = testService.removeProduct(map);
		return new Gson().toJson(resultMap);
	}
	
	// 상품 수정
	@RequestMapping(value = "/update.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String updateList(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = testService.updatePrice(map);
		return new Gson().toJson(resultMap);
	}
	
	// 상품 추가
	@RequestMapping(value = "/insert.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String insertList(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = testService.insertProduct(map);
		return new Gson().toJson(resultMap);
	}
	
	// 상품 리스트 및 검색
	@RequestMapping(value = "/searchList.dox", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
	@ResponseBody
	public String searchList(Model model, @RequestParam HashMap<String, Object> map) throws Exception {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		resultMap = testService.getListSearch(map);
		return new Gson().toJson(resultMap);
	}
}


