package com.minedu.usi.msusi.controller;

import com.minedu.usi.msusi.domain.service.TeacherObjectService;
import com.minedu.usi.msusi.model.TeacherObject;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/teacherObjects")
public class TeacherController {

    private final TeacherObjectService teacherObjectService;

    public TeacherController(TeacherObjectService teacherObjectService) {
        this.teacherObjectService = teacherObjectService;
    }

    @PostMapping
    public TeacherObject saveTeacherObject(@RequestBody TeacherObject teacherObject) {
        return teacherObjectService.saveTeacherObject(teacherObject);
    }

    @GetMapping
    public Iterable<TeacherObject> getTeacherObjects() {
        return teacherObjectService.getAll();
    }
}
