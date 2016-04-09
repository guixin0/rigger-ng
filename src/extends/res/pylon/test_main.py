import  re , os , string ,  getopt ,sys , unittest,logging

def setup_env() :
    root  = os.path.dirname(os.path.realpath(__file__))
    root  = os.path.dirname(root)
    root  = os.path.dirname(root)
    root  = os.path.dirname(root)
    root  = os.path.dirname(root)
    # print(root)
    sys.path.append(os.path.join(root,"src") )
    sys.path.append(os.path.join(root,"src/core") )
    sys.path.append(os.path.join(root,"test") )
    sys.path.append(os.path.join(root,"src/extends/res") )
    os.environ['PRJ_ROOT'] = os.environ['HOME'] + "/devspace/rigger-ng"
    logging.basicConfig(level=logging.DEBUG,filename='test.log')

    import  setting,rg_env,utls.rg_var
    rg_env.rgenv_enable()
    utls.rg_var.import_dict(setting.rgenv)

if __name__ == '__main__':

    setup_env()

    import interface,impl
    impl.setup()
    import pylon
    pylon.setup()

    from pylon_tc   import *
    from parser_tc  import *
    unittest.main()
