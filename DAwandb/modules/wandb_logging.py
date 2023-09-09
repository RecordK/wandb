import wandb

def wandb_logging(args):
    wandb.login() # wandb login 복사한 api 붙여넣기
    
    wandb.init(
        # project가 없으면 wandb에서 새로 생성
        # 기존에 등록된 project가 있으면 같은 project끼리 묶어 실험 결과를 비교
        project=args.project_name,
        name=args.task_name,
        entity=args.entity
        # notes="baseline",
        # tags=["custom loss", "custom optimizer"],
    )
    
    # config 설정
    cfg = {
    "learning_rate": args.lr,
    "epochs": args.epoch,
    "batch_size": args.batch_size
    }
    wandb.config.update(cfg)
    
    # wandb.config에 담긴 파라미터 값들은 wandb 웹에서 모두 확인 가능.
    # wandb.config.update({"drop_rate":0.5})