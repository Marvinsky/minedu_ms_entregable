package com.minedu.usi.msusi.domain.service;

import com.minedu.usi.msusi.model.TeacherObject;

public interface TeacherObjectService {

    public TeacherObject saveTeacherObject(TeacherObject teacherObject);

    public Iterable<TeacherObject> getAll();

}
