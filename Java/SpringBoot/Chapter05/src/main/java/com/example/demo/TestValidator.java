package com.example.demo;

import com.example.demo.User2;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.validation.Valid;

@Controller
public class TestValidator {

    @GetMapping("/test")
    public String showForm(User2 user) {
        return "form";
    }

    @GetMapping("/results")
    public String results() {
        return "results";
    }

    @PostMapping("/test")
    public String checkUser(@Valid User2 user, BindingResult bindingResult, RedirectAttributes attr) {
        if (bindingResult.hasErrors()) {
            return "form";
        }
        
        /**
         * @Description:
         * 1.使用 RedirectAttributes 的 addAttribute 方法传递参数会跟随在 URL 后面
         * 2.使用 addFlashAttribute 不会跟随在 URL 后面，会把该参数值暂时保存于 session，待重定向 url 获取该参数后从 session 中移除，
         * 这里的 redirect 必须是方法映射路径。你会发现 redirect 后的值只会出现一次，刷新后不会出现了,对于重复提交可以使用此来完成。
         */
        attr.addFlashAttribute("user", user);
        return "redirect:/results";

    }
}
 