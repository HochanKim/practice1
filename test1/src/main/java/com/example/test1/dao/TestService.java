package com.example.test1.dao;

import java.util.HashMap;

import com.example.test1.model.Test;

public interface TestService {
	// 상품 불러오기
	HashMap<String, Object> getProductInfo(HashMap<String, Object> map);
	// 상품 삭제
	HashMap<String, Object> removeProduct(HashMap<String, Object> map);
	// 상품 수정
	HashMap<String, Object> updatePrice(HashMap<String, Object> map);
	// 상품 추가
	HashMap<String, Object> insertProduct(HashMap<String, Object> map);
	// 상품 리스트 및 검색
	HashMap<String, Object> getListSearch(HashMap<String, Object> map);
}
