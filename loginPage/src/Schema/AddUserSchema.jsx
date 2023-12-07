import * as Yup from 'yup';
export const AddUserSchema = Yup.object().shape({
    username: Yup.string().min(3, "Username must be at least 3 characters long").required("Please Enter Username"),
    password: Yup.string().required("Please Enter Valid Password"),
    email: Yup.string().email('Invalid email address').required('Email is required'),

});
