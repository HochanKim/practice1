package com.example.test1.mapper;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.example.test1.model.Test;

@Mapper
public interface TestMapper {
	// 상품 가져오기
	Test getProductInfo(HashMap<String, Object> map);
	// 상품 삭제
	void removeProduct(HashMap<String, Object> map);
	// 상품 수정
	void updatePrice(HashMap<String, Object> map);
	// 상품 추가
	void insertProduct(HashMap<String, Object> map);
	// 상품 리스트 및 검색
	List<Test> getListSearch(HashMap<String, Object> map);
}
