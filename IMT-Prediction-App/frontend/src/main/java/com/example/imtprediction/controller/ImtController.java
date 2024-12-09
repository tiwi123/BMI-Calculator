package com.example.imtprediction.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import org.springframework.web.client.RestTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;

@Controller
public class ImtController {

    @PostMapping("/calculate")
    public String calculateImt(@RequestParam double weight, @RequestParam double height, Model model) {
        String url = "http://localhost:5000/calculate_imt";
        
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        
        String json = String.format("{\"weight\": %f, \"height\": %f}", weight, height);
        HttpEntity<String> entity = new HttpEntity<>(json, headers);
        
        ResponseEntity<String> response = restTemplate.postForEntity(url, entity, String.class);
        
        model.addAttribute("result", response.getBody());
        return "index";
    }
}