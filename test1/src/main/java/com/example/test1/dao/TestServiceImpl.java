package com.example.test1.dao;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.test1.mapper.TestMapper;
import com.example.test1.model.Test;

@Service
public class TestServiceImpl implements TestService{

	@Autowired
	TestMapper testMapper;

	@Override
	public HashMap<String, Object> getProductInfo(HashMap<String, Object> map) {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		Test fruit = testMapper.getProductInfo(map);
		resultMap.put("fruit", fruit);
		System.out.println("불러올 상품번호 : "+map);
		return resultMap;
	}

	@Override
	public HashMap<String, Object> removeProduct(HashMap<String, Object> map) {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		testMapper.removeProduct(map);
		System.out.println("삭제할 상품번호 : "+map);
		return resultMap;
	}

	@Override
	public HashMap<String, Object> updatePrice(HashMap<String, Object> map) {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		testMapper.updatePrice(map);
		System.out.println("수정할 상품번호와 가격 : "+map);
		return resultMap;
	}

	@Override
	public HashMap<String, Object> insertProduct(HashMap<String, Object> map) {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		testMapper.insertProduct(map);
		System.out.println("추가할 상품명과 가격 : "+map);
		return resultMap;
	}

	@Override
	public HashMap<String, Object> getListSearch(HashMap<String, Object> map) {
		HashMap<String, Object> resultMap = new HashMap<String, Object>();
		List<Test> list = testMapper.getListSearch(map);
		resultMap.put("list", list);
		return resultMap;
	}

}
