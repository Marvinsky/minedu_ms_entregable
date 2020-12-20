package com.minedu.usi.msusi.domain.service.impl;

import com.minedu.usi.msusi.domain.service.TeacherObjectService;
import com.minedu.usi.msusi.model.TeacherObject;
import com.minedu.usi.msusi.repository.TeacherObjectRepository;
import org.springframework.stereotype.Service;

@Service
public class TeacherObjectServiceImpl implements TeacherObjectService {

    private final TeacherObjectRepository teacherObjectRepository;

    public TeacherObjectServiceImpl(TeacherObjectRepository teacherObjectRepository) {
        this.teacherObjectRepository = teacherObjectRepository;
    }

    @Override
    public TeacherObject saveTeacherObject(TeacherObject teacherObject) {
        return teacherObjectRepository.save(teacherObject);
    }

    @Override
    public Iterable<TeacherObject> getAll() {
        return teacherObjectRepository.findAll();
    }
}
